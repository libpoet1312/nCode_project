from datetime import datetime
import calendar

from werkzeug.exceptions import BadRequest

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
        raise BadRequest(description=str(error))

    return calendar.timegm(datetime_obj.utctimetuple())