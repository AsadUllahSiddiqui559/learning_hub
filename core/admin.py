from django.contrib import admin

from .models import Teacher, Class, Student

admin.site.register(Teacher)
admin.site.register(Class)
admin.site.register(Student)