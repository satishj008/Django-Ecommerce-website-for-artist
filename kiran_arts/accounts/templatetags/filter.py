from products.models import Category
from django import template

register = template.Library()

@register.filter(name='servicefilter')
def servicefilter(p,s):
    return p.filter(service=s)



@register.filter(name='acf')

def acf(v):  
    if v.name=="Basic":  
        return "show active"
    return ""


@register.filter(name='catfilter')
def catfilter(s,i):
    return s.filter(subcategory__category=i).distinct()




