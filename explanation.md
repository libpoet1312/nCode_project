# Study Case Explanation

So the provided endpoint is /api/v1/stackstats.

It can handle 2 query parameters (since, until=optional). Both query parameters must be in a format
of _%Y-%m-%d %H:%M:%S_ otherwise a 400 is returned.

All business logic is under _app/consumer/consumer.py_.

1. We get all answers for the given time range in a List and then we sort them based on their score.

2. We get the accepted answers by filtering the answers List.
3. We calculate the avg score with the help of statistics library.
4. With the help of comments API endpoint provided by StackExchange we calculate the **top_10_answers_comment_count**.
5. We calculate the **average_answers_per_question** by building a questions object (Dict).
questions object: <br/>
```
    questions = {
        question_id : number of answers
        ...
        ...
    }   
```
6. We calculate the **average_answers_per_question** from the above questions object.
    
