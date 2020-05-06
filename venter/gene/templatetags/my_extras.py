from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):

    """

    This cuts out all values of "arg" from the string

    """
    return value.replace(arg,'')

# can be a decorator
#register.filter('cut',cut)
#what you wanna call the thing in str, cut is the Function
