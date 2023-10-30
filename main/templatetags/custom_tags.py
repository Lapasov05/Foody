from django import template

register = template.Library()


@register.simple_tag
def calculate_total(count, price):
    return int(count) * int(price)