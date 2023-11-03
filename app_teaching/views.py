from django.shortcuts import render
from . import models
from django.views import generic
from django.db.models import Q
from .models import Course,Person
from . import forms
from django.db.models import Value
from django.db.models.functions import Concat

# Create your views here.

def is_valid_queryparam(param):
    return param != '' and param is not None

def index(request):
    return render(request,'index.html')
def admin(request):
    return render(request,'admin.html')
def about(request):
    return render(request,'about.html')

def courses(request):
    all_courses = models.Course.objects.all()
    return render(request,'courses.html',{'courses': all_courses})

def persons(request):
    all_persons= models.Person.objects.all()
    return render(request,'persons.html',{'persons': all_persons})

def personcourse(request):
    all_personcourse= models.PersonCourse.objects.all()
    print('all_personcourse',all_personcourse)
    return render(request,{'personcourse': all_personcourse})


class CourseDetailView(generic.DetailView):
    template_name = 'course_details.html'
    model = models.Course
    context_object_name = 'course'
    
class PersonDetailView(generic.DetailView):
    template_name = 'person_details.html'
    model = models.Person
    context_object_name = 'person'




#  def BootstrapFilterView(request):
#     qs = Course.objects.all()
    
#     name_or_id_contains_query = request.GET.get('name_or_id_contain')
#     description_contains_query = request.GET.get('description_contains')
    
#     date_min = request.GET.get('date_min')
#     date_max = request.GET.get('date_max')
#     pro_type = request.GET.get('pro_type')
#     keyword = request.GET.get('keyword')
#     persons= Person.objects.all()


#     person = request.GET.get('person')
 

#     categories = Course.objects.values_list('type', flat=True).distinct()
#     print(categories)
    
#     if name_or_id_contains_query!= '' and name_or_id_contains_query is not None:
#         qs = qs.filter(Q(project_id__icontains=name_or_id_contains_query) | Q(name__icontains=name_or_id_contains_query)).distinct()


#     elif description_contains_query != '' and description_contains_query is not None:
#         qs = qs.filter(description__icontains=description_contains_query)



    

#     if is_valid_queryparam(date_min) :
#         qs = qs.filter(start_date__gte=date_min)
   
#     if is_valid_queryparam(date_max) :
#         qs = qs.filter(start_date__lt=date_max)

#     if is_valid_queryparam(pro_type) and pro_type != 'Choose...' :
#         qs = qs.filter(type=pro_type)

#     if is_valid_queryparam(keyword) and keyword != 'Choose...' :
#         qs = qs.filter(keywords__icontains=keyword)


#     if is_valid_queryparam(person) and person != 'Choose...':
#         qs = qs.filter(persons__first_name__icontains=person.split(" ")[0], persons__last_name__icontains=person.split(" ")[-1])


#     context = {
#         'queryset' :qs,
#         'persons' :persons,
#         'categories':categories,


#     }

#     return render(request, "bootstrap_form.html",context)
