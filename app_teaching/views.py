from django.shortcuts import render
from . import models
from django.views import generic
from django.db.models import Q
from .models import Course,Person,PersonCourse
from . import forms
from django.db.models import Value
from django.db.models.functions import Concat
from django.http import HttpResponse
from django.template import loader




# Create your views here.

def is_valid_queryparam(param):
    return param != '' and param is not None

def index(request):
    return render(request,'index.html')


def plot(request):
    courses = Course.objects.all()
    personcourses = PersonCourse.objects.all()
    context ={
        "courses": courses,
        "personcourses":personcourses
    }
    return render(request,'app_teaching/index.html',context)



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

# def personcourse(request):
#     all_personcourse= models.PersonCourse.objects.all()
#     return render(request,'person_details.html', {'personcourse': all_personcourse})

def personcourse(request):
    context = {
    'all_personcourse':PersonCourse.objects.all()
    }
    return render(request, 'personcourse_details.html', context)



def courseperson(request):
    context = {
    'coursepersons':PersonCourse.objects.all()
    }
    return render(request, 'courseperson.html', context)

def courseperson_s(request):
    all_courses_ses =PersonCourse.objects.all()
    return render(request,'courseperson_s.html',{'coursepersons': all_courses_ses})

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
    course_type = request.GET.get('course_type')
    course_groupe = request.GET.get('course_groupe')

    persons= Person.objects.all()
    person = request.GET.get('person')
 
    qs2=PersonCourse.objects.all()
    
    categories = Course.objects.values_list('type', flat=True).distinct()
    print('cat',categories)
    # categories=categories.exclude(type='MS').exclude(type='FP')
    groups = Course.objects.values_list('group', flat=True).distinct()
    print('groups',groups)  

    if is_valid_queryparam(person) and person != 'Choose...':
        qs2 = qs2.filter(person__first_name__icontains=person.split(" ")[0], person__last_name__icontains=person.split(" ")[-1])
        print('qs',qs)   

    if is_valid_queryparam(course_type) and course_type != 'Choose...' :
        qs = qs.filter(type=course_type)

    if is_valid_queryparam(course_groupe) and course_groupe != 'Choose...' :
        qs = qs.filter(group=course_groupe)

    context = {
        'queryset' :qs,
        'persons' :persons,
        'categories':categories,
        'groups':groups,
        'personcourse':qs2,

    }

    return render(request, "bootstrap_form.html",context)


