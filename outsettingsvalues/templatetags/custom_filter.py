"""
File with custom tags.
"""
from django import template

register = template.Library()


@register.simple_tag
def checkdict(args):
    """
    Check type of args. Dict or not.

    """
    return isinstance(args, dict)


@register.simple_tag
def checklist(args):
    """
    Check type of args. List or Tuple or another.

    """
    return isinstance(args, list) or isinstance(args, tuple) or isinstance(args, set)
