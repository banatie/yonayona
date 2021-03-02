from datetime import time, datetime
import pytz

from ..config.availability import hours_limitation


def is_available():
    if not hours_limitation['is_enabled']:
        return True

    hours_from = time(hours_limitation['hours_from'], 0, 0)
    hours_to = time(hours_limitation['hours_to'], 0, 0)
    local_timezone = pytz.timezone(hours_limitation['timezone'])
    if hours_from <= datetime.now(tz=local_timezone).time() <= hours_to:
        return True

    return False

def get_working_hours_str():
    if not hours_limitation['is_enabled']:
        return None

    hours_from = time(hours_limitation['hours_from'], 0, 0)
    hours_to = time(hours_limitation['hours_to'], 0, 0)
    return '{hours_from}{hours_from_am_pm} - {hours_to}{hours_to_am_pm}'.format(
        hours_from=hours_from.hour, hours_from_am_pm=hours_from.strftime('%p').lower(),
        hours_to=hours_to.hour, hours_to_am_pm=hours_to.strftime('%p').lower()
    )
