from django.template import Library

from timezones.utils import adjust_datetime_to_timezone, localtime_for_timezone

register = Library()

def localtime(value, timezone):
    return value and localtime_for_timezone(value, timezone) or value
register.filter("localtime", localtime)

def from_localtime(value, timezone):
    return adjust_datetime_to_timezone(value, timezone)
register.filter("from_localtime", from_localtime)
