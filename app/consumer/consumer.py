import logging
import statistics
from time import sleep
import requests
from urllib.parse import urlencode
from collections import Counter

from connexion.exceptions import ProblemException

from app.consumer.helpers import checkFormatAndGetTimeStamp

ANSWERS_BASE_URL = "https://api.stackexchange.com/2.3/answers"
COMMENTS_BASE_URL = 'https://api.stackexchange.com/2.3/answers/'


class Consumer:
    def _call_answers_api(self, query_params, all_results):
        api_url = ANSWERS_BASE_URL + '?' + urlencode(query_params)

        items = []
        has_more = True
        while has_more:
            response = requests.get(api_url)
            if response.status_code != 200:
                print(response.json())
                raise ProblemException(detail='StackExchange not responding')

            response = response.json()
            items += response['items']
            has_more = True if 'has_more' in response and response['has_more'] else False

            if not has_more or query_params['page'] >= 25 or not all_results:
                break

            query_params['page'] += 1
            api_url = ANSWERS_BASE_URL + '&' + urlencode(query_params)
            sleep(2)  # Sleep to prevent back off ( rate limiting by StackExchange )
        return items

    def _getResponseFromApi(self, since_timestamp, until_timestamp, all_results):
        query_params = {
            'site': 'stackoverflow',
            'fromdate': str(since_timestamp),
            'page_size': 100,
            'sort': 'votes',
            'order': 'desc',
            'page': 1
        }

        if until_timestamp:
            query_params['todate'] = str(until_timestamp)

        return self._call_answers_api(query_params, False)

    def _getCommentsByAnswerId(self, _id):
        query_params = {
            'site': 'stackoverflow',
            'page_size': 100,
            'sort': 'creation',
            'order': 'desc',
        }

        api_url = COMMENTS_BASE_URL + _id + '/comments' + '?' + urlencode(query_params)
        response = requests.get(api_url)
        if response.status_code != 200:
            print(response.json())
            raise ProblemException(detail='StackExchange not responding')

        response = response.json()
        return sorted(response['items'], key=lambda d: d['score'], reverse=True)

    def expose(self, since, until=None, get_all_results_from_pagination=False):
        since_timestamp = checkFormatAndGetTimeStamp(since)
        until_timestamp = checkFormatAndGetTimeStamp(until)

        answers = self._getResponseFromApi(since_timestamp, until_timestamp, get_all_results_from_pagination)

        sorted_answers_by_score = sorted(answers, key=lambda d: d['score'], reverse=True)

        # Accepted answers
        accepted_answers = [answer for answer in sorted_answers_by_score if answer['is_accepted']]
        accepted_answers_average_score = statistics.mean([answer['score'] for answer in accepted_answers])

        top_10_answers_comment_count = {
            answer['answer_id']: len(
                self._getCommentsByAnswerId(str(answer['answer_id']))
            ) for answer in sorted_answers_by_score[:10]
        }

        # Build questions object
        # question_id: number of answers
        questions = Counter()
        for answer in sorted_answers_by_score:
            questions[answer['question_id']] += 1

        # Average
        average_answers_per_question = statistics.mean(questions[question_id] for question_id in questions)

        return {
            "total_accepted_answers": len(accepted_answers),
            "accepted_answers_average_score": accepted_answers_average_score,
            "average_answers_per_question": average_answers_per_question,
            "top_ten_answers_comment_count": top_10_answers_comment_count,
        }
