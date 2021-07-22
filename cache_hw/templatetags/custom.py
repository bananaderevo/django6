from random import randint

from django import template
import requests
from bs4 import BeautifulSoup
register = template.Library()
from django.core.cache import cache


@register.filter(name='censoring')
def censoring(value, list1):
    value2 = []
    for i in value.split(' '):
        if i.lower().replace(',', '').replace('.', '').replace('"', '') in list1:
            value2.append('***')
        else:
            value2.append(i)
    return ' '.join(value2)


@register.simple_tag
def rand_quote(quo):
    return quo.get(id=randint(0, quo.all().last().id))
