from django import template

from accounts.models import Course

register = template.Library()


@register.filter(name='courses')
def courses(semester_no):
    return Course.objects.filter(semester_no=semester_no)
