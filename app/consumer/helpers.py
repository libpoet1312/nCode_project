from datetime import datetime
import calendar

from connexion.exceptions import BadRequestProblem, ProblemException


def checkFormatAndGetTimeStamp(time_date_str):
    """
    Function to check time_date given format
    And convert it to UNIX timestamp
    :param time_date_str:
    :return: Unix timestamp
    :raises: BadRequest
    """
    if not time_date_str:
        return None

    try:
        datetime_obj = datetime.strptime(time_date_str, '%Y-%m-%d %H:%M:%S')
    except ValueError as error:
        raise BadRequestProblem(detail=str(error))

    return calendar.timegm(datetime_obj.utctimetuple())