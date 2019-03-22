from django import template
register = template.Library()


@register.simple_tag
def dan(data):
    for i in data:
        return i
