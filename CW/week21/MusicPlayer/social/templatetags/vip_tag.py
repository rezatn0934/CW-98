from django import template
from django.contrib.auth.models import Group

register = template.Library()


@register.filter(name='has_vip_perm')
def has_vip_perm(user, group_name):
    group = Group.objects.filter(name=group_name.upper())
    if group:
        group = group.first()
        return group in user.groups.all()
    else:
        return False
