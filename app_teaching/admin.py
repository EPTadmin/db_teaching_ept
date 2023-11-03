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

    list_display = [field.name for field in Course._meta.get_fields() if ((field.name != 'id')) ]
    list_filter_link = ("course_id",) 
    # list_display.append("assigned_persons")
    # list_display.append("assigned_ressources")
    # list_display.append("assigned_partners")

    form = CourseAdminForm
    # search_fields = ('methods','keywords','name','description', "persons__last_name", "persons__first_name")

    # list_filter = ("keywords", "methods","type","groups","persons")

    # @admin.display(description='Persons')
    # def assigned_persons(self, obj):
    #     return format_html("{}", mark_safe([f"<a href='../persons/{person.id}'>{person}</a>" for person in Course]))


    # @admin.display(description='Ressource')
    # def assigned_ressources(self, obj):
    #     return format_html("{}", mark_safe([f"<a href='../ressource/{ressource.id}'>{ressource}</a>" for ressource in obj.ressources.all()]))
    
    # @admin.display(description='Partners')
    # def assigned_partners(self, obj):
    #     return format_html("{}", mark_safe([f"<a href='../partner/{partner.id}'>{partner}</a>" for partner in obj.partners.all()]))
    #     # list_url=[])
        # url =[ressource.location for ressource in obj.ressources.all()]
        # print(url)
        # all_url ={}
        # all_text={}

        # for a in range(len(url)):
        #     print(a)
        #     all_url[a] ='<a href="%s">%s,</a>' % (url[a],obj.ressources.all()[a]) 
        # print('all url',all_url)

        # return format_html( all_url[0])        
        # # return format_html("<a href='{url}'>{}</a>",url=[ressource.location for ressource in obj.ressources.all()],obj.ressources.all())
        # list_url=[]
        # list_name=[]
        # url = [ressource.location for ressource in obj.ressources.all()]
        # for a in range(0,len(url)):
        #     print(a)
        #     print('a',url[a])
        #     print('b',obj.ressources.all()[a])
        #     list_url.append(url[a])
        #     list_name.append(obj.ressources.all()[a])
        # print(list_name,list_url)
        
        # return format_html("<a href='{url}'>{text}</a>", 
        #                        url = list_url,text='test')
        #print('liste complete',url,len(url))
        # for a in range(0,len(url)):
        #     print(url[a],obj.ressources.all())
        #for a in range(0,len(obj.ressources.all())):
            #print('a',a,obj.ressources.all()[a])
        #return format_html(u'<a href="{}">{}</a>', 
                               #url[0],  obj.ressources.all()[0])
        # list_url = []
        # list_name =[]
        # for a, b in zip(range(len(url)), range(len(obj.ressources.all()))):
        #     print(url[a])
        #     print(obj.ressources.all()[b])
        #     list_url.append(url[a])
        #     list_name.append(obj.ressources.all()[b])

        
        # return format_html(u'<a href="{}"</a>'.format(list_url, list_name))
            # print(url[a],obj.ressources.all()[a])
            # for a in range(0,len(obj.ressources.all())):
            #      print(obj.ressources.all()[a])
            # list_url.append(url[a])
            # list_name.append(obj.ressources.all()[0])
        # print('url',list_url,'name',list_name)
        # return format_html(u'<a href="{}">{}</a>', 
        #                           list_url,  list_name)


class PersonAdmin(admin.ModelAdmin):

    list_display = [field.name for field in Person._meta.get_fields() if ((field.name != 'id') and (field.name != 'middle_name')) ][:-1]
    form = CourseAdminForm
    list_display.append("assigned_course")
    # list_display.append("amount")

    @admin.display(description='Course')
    def assigned_course(self, obj):
        return format_html("{}", mark_safe([f"<a href='../course/{course.id}'>{course}</a>" for course in obj.courses.all()]))

    # @admin.display(description='Amount')
    # def amount(self, obj):
    #     return format_html("{}", mark_safe([f"<a href='../personcourse/{amount.id}'>{amount}</a>" for amount in obj.personcourse.all()]))


# class PersonToCourseAdmin(admin.ModelAdmin):

#     list_display = [field.name for field in PersonToCourse._meta.get_fields() if ((field.name != 'id'))]
#     form = CourseAdminForm

    # @admin.display(description='Course')
    # def assigned_course(self, obj):
    #     return format_html("{}", mark_safe([f"<a href='../course/{course.id}'>{course}</a>" for course in obj.courses.all()]))

admin.site.register(Course, CourseAdmin)
admin.site.register(Person,PersonAdmin)
admin.site.register(PersonCourse)
# admin.site.register(Partner)
# admin.site.register(Ressource)