from django.contrib import admin
from .models import *
from .forms import *
from .views import personcourse
from django import forms
from django.db.models import Value
from django.db.models.functions import Concat
from django.utils.html import format_html
from django.utils.safestring import mark_safe
import pandas as pd
# Register your models here.


class CourseAdmin(admin.ModelAdmin):

    list_display = [field.name for field in Course._meta.get_fields() if ((field.name != 'personcourse') and (field.name != 'id') and (field.name !='courses') and (field.name != 'course_amount')) ]
    list_filter_links = ('course_id','name') 
    list_filter = ("type","group", )

    # list_display.append("assigned_ressources")
    # a =  [PersonCourse.objects.prefetch_related('course')]
    
    form = CourseAdminForm

    # @admin.display(description='Amount')

    # def total_amount(self, obj):
    #     a = Course.objects.all().values('course_id')
    #     for b in a:
    #         total=0
    #         print('course id ',b['course_id'])
    #         p = PersonCourse.objects.filter(course__course_id= b['course_id']).prefetch_related('person') 
    #         print('p',p)
    #         # p = PersonCourse.objects.filter(course__course_id= 'TEP4111').prefetch_related('person') 

    #         for a in p :
    #             # print(float(a.amount))
    #             total += float(a.amount)
    #         print(total)
    #     return total
    
    # @admin.display(description='Amount')
    # def total_amount(self, obj):
    #     return [f"<a href='../personcourse/{course.id}'>{[PersonCourse.objects.filter(course__course_id= course.id).prefetch_related('person') ]}</a>" for course in obj.courses.all()]

    # @admin.display(description='Person')
    # def assigned_person(self, obj):
    #     return format_html("{}", mark_safe([f"<a href='../person/{person.id}'>{person}</a>" for person in obj.person.all()]))
    


class PersonAdmin(admin.ModelAdmin):

    list_display = [field.name for field in Person._meta.get_fields() if ((field.name != 'personcourse') and(field.name != 'id') and (field.name != 'middle_name')and (field.name != 'person_amount')) ][:-1]
    list_filter = ("groupe", )
    list_display_links = ('first_name', 'last_name')

    # for field in Person._meta.get_fields():
    #     print(field.name)
    form = CourseAdminForm
    # list_display.append("full_name")

    # list_display.append("assigned_course")
    list_display.append("assigned_amount_O1")
    # print(list_display)

    list_display.append("assigned_amount_O2")
    list_display.append("assigned_Belast_Tid")
    list_display.append("assigned_Belast_fde")
    list_display.append("assigned_pourcent_75")
    list_display.append("assigned_student")
    list_display.append("assigned_Belast_fdeb")
    list_display.append("assigned_student_msc")
    list_display.append("assigned_Belast_msc")
    list_display.append("assigned_Belast_phd")

    # @admin.display(description='Amount')
    # def assigned_amount(self, obj):
    #     return ([a.amount for a in  PersonCourse.objects.filter(person__id = obj.id)])
    
    @admin.display(description='Amount_O1')
    def assigned_amount_O1(self, obj):
        print('personcourse',PersonCourse.objects.filter(course__type ='O1'))
        return round(sum([(a.amount)/100*280 for a in  PersonCourse.objects.filter(person__id = obj.id).filter(course__type ='O1')]))
    
    @admin.display(description='Amount_O2')
    def assigned_amount_O2(self, obj):
        return round(sum([(a.amount)/100*252 for a in  PersonCourse.objects.filter(person__id = obj.id).filter(course__type ='O2')]))
    
    @admin.display(description='Belast_Tid_7.5')
    def assigned_Belast_Tid(self, obj):
        a=[(a.amount)/100*280 for a in  PersonCourse.objects.filter(person__id = obj.id).filter(course__type ='O1')]
        b=[(a.amount)/100*252 for a in  PersonCourse.objects.filter(person__id = obj.id).filter(course__type ='O2')]
        c=sum(pa for pa in a)+sum(pb for pb in b)
        return round(c)
    
    @admin.display(description='% 7.5')
    def assigned_pourcent_75(self, obj):
        a=[(a.amount)/100*280 for a in  PersonCourse.objects.filter(person__id = obj.id).filter(course__type ='O1')]
        b=[(a.amount)/100*252 for a in  PersonCourse.objects.filter(person__id = obj.id).filter(course__type ='O2')]
        c=sum(pa for pa in a)+sum(pb for pb in b)
        return round(c/250*100)       
    
    @admin.display(description='Belast_Tid_FDE')
    def assigned_Belast_fde(self, obj):
        a=[(a.amount) for a in  PersonCourse.objects.filter(person__id = obj.id).filter(course__type ='FE')]
        b=[(float(a.course.studiepoeng.replace(',','.'))) for a in PersonCourse.objects.filter(person__id = obj.id).filter(course__type ='FE')]
        c=sum(((pa))*((pb)) for pa, pb in zip(a,b))        
        return (c/(100*3.75)*125)
    
    @admin.display(description='Ant. Stud.')
    def assigned_student(self, obj):
        a=[float(a.amount) for a in  PersonCourse.objects.filter(person__id = obj.id).filter(course__type ='FP')]
        return int(sum(pa for pa in a)) 
    
    @admin.display(description='Belast_Tid_FDEB')
    def assigned_Belast_fdeb(self, obj):
        timer  =timer_75=0
        studiepoeng=[float(a.course.studiepoeng.replace(',','.')) for a in  PersonCourse.objects.filter(person__id = obj.id).filter(course__type ='FP')]
        print(studiepoeng)
        nb_stud = [float(a.amount) for a in  PersonCourse.objects.filter(person__id = obj.id).filter(course__type ='FP')]
        print(a for a in nb_stud)
        print(b for b in studiepoeng)
        timer_75 = sum ((pa)* 30 for pa, pb in zip(nb_stud,studiepoeng) if pb==float(7.5)) 
        timer_15 = sum ((pa)* 40 for pa, pb in zip(nb_stud,studiepoeng) if pb==float(15)) 
        timer_20 = sum ((pa)* 50 for pa, pb in zip(nb_stud,studiepoeng) if pb==float(20)) 

        # ((pa)* 40 for pa, pb in zip(nb_stud,studiepoeng) if pb==float(15)) , ((pa)* 50 for pa, pb in zip(nb_stud,studiepoeng) if pb==float(20))


        return (timer_75+timer_15+timer_20)
    
    @admin.display(description='Ant. Stud. MSc')
    def assigned_student_msc(self, obj):
        a=[float(a.amount) for a in  PersonCourse.objects.filter(person__id = obj.id).filter(course__type ='MS')]
        return int(sum(pa for pa in a)) 
    
    @admin.display(description='Belast_Tid_MSC')
    def assigned_Belast_msc(self, obj):
        a=[(a.amount) for a in  PersonCourse.objects.filter(person__id = obj.id).filter(course__type ='MS')]
        b=[(float(a.course.studiepoeng.replace(',','.'))) for a in PersonCourse.objects.filter(person__id = obj.id).filter(course__type ='MS')]
        c=sum(((pa))*((pb)) for pa, pb in zip(a,b))        
        return int(c)
    
    @admin.display(description='Belast_Tid_PHD')
    def assigned_Belast_phd(self, obj):
        a=[1 for a in  PersonCourse.objects.filter(person__id = obj.id).filter(course__type ='PH') if a!=0]                
        return int(sum(pa*250 for pa in a))
    # @admin.display(description='Amount')
    # def assigned_amount(self, obj):
    #     for course in Course.objects.all():
    #         print(course.course_id)
    #     return ([{a.amount} for a in  PersonCourse.objects.filter(course__course_id__icontains= 'TEP4110').filter(course__name__icontains = 'Fluidmekanikk').filter(person__first_name__icontains = 'Tania')])
    

    
# (course for course in obj.courses.all())
# ,person__last_name__icontains='Bracchi'
class PersonCourseAdmin(admin.ModelAdmin):
#     for a in PersonCourse.objects.all():
#         print('a',a)

    list_display = [field.name for field in PersonCourse._meta.get_fields() if (field.name != 'id')]
    # list_display.append("assigned_course")

    # list_display = ["assigned_course"]
    # for a in list_display:
    #     print(a)
    form = CourseAdminForm
    # list_display.append("assigned_person")
    # list_display.append("assigned_group")

#     list_display = ["assigned_person","assigned_group","assigned_course","amount"]
#     list_filter = ("person__groupe","person", "course",)
#     print(list_display)

    # @admin.display(description='Course')
    # def assigned_course(self, obj):
    #     return format_html("{}", mark_safe([f"<a href='../course/{course.id}'>{course}</a>" for course in obj.course.all()]))
    
    # @admin.display(description='Person')
    # def assigned_person(self, obj):
    #     return [PersonCourse.__get__(obj.person.person_id)]
    
#     @admin.display(description='Group')
#     def assigned_group(self, obj):
#         return [person.groupe for person in obj.person.all()]

admin.site.register(Course, CourseAdmin)
admin.site.register(Person,PersonAdmin)
# admin.site.register(PersonCourse,PersonCourseAdmin)
admin.site.register(PersonCourse,PersonCourseAdmin)
# admin.site.register(Ressource)