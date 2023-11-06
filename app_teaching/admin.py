from django.contrib import admin
from .models import *
from .forms import *
from django import forms
from django.db.models import Value
from django.db.models.functions import Concat
from django.utils.html import format_html
from django.utils.safestring import mark_safe

# Register your models here.


class CourseAdmin(admin.ModelAdmin):

    list_display = [field.name for field in Course._meta.get_fields() if ((field.name != 'id') and (field.name !='courses') and (field.name != 'course_amount')) ]
    list_filter_link = ("course_id",) 
    # list_display.append("assigned_persons")
    # list_display.append("assigned_ressources")
    # list_display.append("assigned_partners")

    form = CourseAdminForm
    


class PersonAdmin(admin.ModelAdmin):

    list_display = [field.name for field in Person._meta.get_fields() if ((field.name != 'id') and (field.name != 'middle_name')and (field.name != 'person_amount')) ][:-1]
    form = CourseAdminForm
    list_display.append("assigned_course")
    list_display_links=("first_name","last_name",)
    print(list_display)

    @admin.display(description='Course')
    def assigned_course(self, obj):
        return format_html("{}", mark_safe([f"<a href='../course/{course.id}'>{course}</a>" for course in obj.courses.all()]))

    # @admin.display(description='Amount')
    # def amount(self, obj):
    #     return format_html("{}", mark_safe([f"<a href='../personcourse/{amount.id}'>{amount}</a>" for amount in obj.personcourse.all()]))


class PersonCourseAdmin(admin.ModelAdmin):

    list_display = [field.name for field in PersonCourse._meta.get_fields() if ((field.name != 'id') and (field.name != 'person') and (field.name != 'course'))]
    form = CourseAdminForm
    print(list_display)
    list_display.append("assigned_course")
    list_display.append("assigned_person")
    list_display = ["assigned_person","assigned_course","amount"]
    list_filter = ("person", "course",)
    @admin.display(description='Course')
    def assigned_course(self, obj):
        return format_html("{}", mark_safe([f"<a href='../course/{course.id}'>{course}</a>" for course in obj.course.all()]))
    @admin.display(description='Person')
    def assigned_person(self, obj):
        return format_html("{}", mark_safe([f"<a href='../person/{person.id}'>{person}</a>" for person in obj.person.all()]))

admin.site.register(Course, CourseAdmin)
admin.site.register(Person,PersonAdmin)
admin.site.register(PersonCourse,PersonCourseAdmin)
# admin.site.register(Partner)
# admin.site.register(Ressource)