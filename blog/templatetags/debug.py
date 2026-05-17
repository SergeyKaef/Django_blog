from django import template

register = template.Library()

@register.filter
def as_dict(value):
    return value.__dict__