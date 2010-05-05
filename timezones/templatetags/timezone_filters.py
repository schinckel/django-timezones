
from django.template import Node
from django.template import Library

from timezones.utils import localtime_for_timezone

register = Library()

def localtime(value, timezone):
    return value and localtime_for_timezone(value, timezone) or value
register.filter("localtime", localtime)

