from django.shortcuts import render
from . import models
from django.views import generic
from django.db.models import Q
from .models import Course,Person,PersonCourse
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
def courses_ses(request):
    all_courses_ses = models.Course.objects.all()
    return render(request,'courses_ses.html',{'courses_ses': all_courses_ses})
def courses_indecol(request):
    all_courses_indecol = models.Course.objects.all()
    return render(request,'courses_indecol.html',{'courses_indecol': all_courses_indecol})
def courses_process(request):
    all_courses_process = models.Course.objects.all()
    return render(request,'courses_process.html',{'courses_process': all_courses_process})
def courses_thermo(request):
    all_courses_thermo = models.Course.objects.all()
    return render(request,'courses_thermo.html',{'courses_thermo': all_courses_thermo})
def persons(request):
    all_persons= models.Person.objects.all()
    return render(request,'persons.html',{'persons': all_persons})

def personcourse(request):
    all_personcourse= models.PersonCourse.objects.all()
    return render(request,'courses_ses.html',{'personcourses': all_personcourse})


class CourseDetailView(generic.DetailView):
    template_name = 'course_details.html'
    model = models.Course
    context_object_name = 'course'
    
class PersonDetailView(generic.DetailView):
    template_name = 'person_details.html'
    model = models.Person
    context_object_name = 'person'

# class PersonCourseDetailView(generic.DetailView):
#     template_name = 'person_details.html'
#     model = models.PersonCourse
#     context_object_name = 'personcourse'


def BootstrapFilterView(request):
    qs = Course.objects.all()

    persons= Person.objects.all()
    person = request.GET.get('person')
 
    qs2=PersonCourse.objects.all()

    if is_valid_queryparam(person) and person != 'Choose...':
        qs2 = qs2.filter(person__first_name__icontains=person.split(" ")[0], person__last_name__icontains=person.split(" ")[-1])
        print('qs',qs)   


    context = {
        'queryset' :qs,
        'persons' :persons,

    }

    return render(request, "bootstrap_form.html",context)
