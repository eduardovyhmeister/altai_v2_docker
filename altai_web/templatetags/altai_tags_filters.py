from django import template
register = template.Library()

@register.simple_tag
def total_posts():
    return 'Prueba'


@register.filter
def indexing(indexable, i):
    try:
        indexable=eval(indexable)
    except:
        indexable=indexable
    return indexable[i]

@register.filter
def naming(indexable,extra):
    try:
        indexable=indexable+extra
    except:
        indexable=indexable
    return indexable



