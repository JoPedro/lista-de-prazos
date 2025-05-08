from django import template

register = template.Library()


@register.filter(is_safe=True, name="abs")
def absolute(value):
    """Returns the absolute value of an integer"""
    return abs(value)
