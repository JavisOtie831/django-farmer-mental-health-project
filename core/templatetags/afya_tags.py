from django import template

register = template.Library()

@register.filter
def fix_plural(name):
    # If the name ends with 'ss' (like Userss, Roles, etc.), remove the last 's'
    if name.endswith('ss'):
        return name[:-1]
    return name