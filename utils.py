from datetime import datetime
import pytz
import config
import re


def to_izh_time_zone(match):
    time = match.group()
    time_obj = datetime.strptime(time, "%H:%M")

    old_timezone = pytz.timezone(config.moscow_tz)
    new_timezone = pytz.timezone(config.izhevsk_tz)

    # returns datetime in the new timezone
    localized = old_timezone.localize(time_obj).astimezone(new_timezone)

    local_format = "%H:%M"

    return localized.strftime(local_format)


def replace_time_with_local(text):
    return re.sub(r'\d{2}:\d{2}', to_izh_time_zone, text)
