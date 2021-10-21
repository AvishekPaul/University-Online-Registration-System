from django.contrib import admin
from accounts.models import Student, Registration, Course

# Register your models here.

admin.site.register(Student)
admin.site.register(Registration)
admin.site.register(Course)