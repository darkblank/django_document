from django.contrib import admin

from inheritance.models import Teacher, Student, School

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(School)