"""
File with custom tags.
"""
from django import template

register = template.Library()


@register.simple_tag
def checktype(args):
    """
    Check type of args. Dict or not.

    :param args:
    :return: True or False
    """
    return isinstance(args, dict)


@register.simple_tag
def checktypelist(args):
    """
    Check type of args. List or Tuple or another.

    :param args:
    :return: True or False
    """
    return isinstance(args, list) or (args, tuple) or (args, set)
