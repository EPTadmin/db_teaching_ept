from django.shortcuts import render
from . import models
from django.views import generic
from django.db.models import Q
from .models import Course,Person,PersonCourse,PersonActivity
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
    courses = [{'course_id':obj.course_id, 'name':obj.name,'type':obj.type,'group':obj.group,'nb_student':obj.nb_student }for obj in Course.objects.all()]
    personcourses = [{'person_group':obj.person.groupe,'person':obj.person.first_name+ ' ' +obj.person.last_name, 'course_type':obj.course.type, 'course_group':obj.course.group,'course':obj.course.course_id+ ' ' +obj.course.name,'amount':obj.amount}for obj in PersonCourse.objects.all()]
    print(personcourses)
    context ={
        "courses": courses,
        "personcourses":personcourses
    }
    return render(request,'app_teaching/index.html',context)

def nb_student(request):
    courses = [{'course_id':obj.course_id, 'name':obj.name,'type':obj.type,'group':obj.group,'nb_student':obj.nb_student }for obj in Course.objects.all()]
    context ={
        "courses": courses
    }
    return render(request,'app_teaching/index_nb_stud_type.html',context)

def load(request):
    courses = [{'course_id':obj.course_id, 'name':obj.name,'type':obj.type,'group':obj.group,'nb_student':obj.nb_student }for obj in Course.objects.all()]
    persons = [{'name':obj.first_name+ ' ' +obj.last_name,'group':obj.groupe}for obj in Person.objects.all()]
    personcourses = [{'person_group':obj.person.groupe,'person':obj.person.first_name+ ' ' +obj.person.last_name, 'course_type':obj.course.type, 'course_sp':obj.course.studiepoeng,'course_group':obj.course.group,'course':obj.course.course_id+ ' ' +obj.course.name,'amount':obj.amount}for obj in PersonCourse.objects.all()]

    personactivities = [{'person_group':obj.person.groupe,'person':obj.person.first_name+ ' ' +obj.person.last_name, 'activity_type':obj.activity.type,'arsverk':obj.activity.arsverk,'activity_antall_time':obj.activity.antall_time,'activity_emne':obj.activity.emne,'amount':obj.amount}for obj in PersonActivity.objects.all()]
    personactivities_position = [{'person_group':obj.person.groupe,'person':obj.person.first_name+ ' ' +obj.person.last_name, 'activity_type':obj.activity.type,'arsverk':obj.activity.arsverk,'activity_emne':obj.activity.emne,'amount':obj.amount}for obj in PersonActivity.objects.all() if obj.activity.emne == 'L']
    personactivities_project = [{'person_group':obj.person.groupe,'person':obj.person.first_name+ ' ' +obj.person.last_name, 'activity_type':obj.activity.type,  'activity_antall_time':obj.activity.antall_time,'activity_emne':obj.activity.emne,'amount':obj.amount}for obj in PersonActivity.objects.all()if obj.activity.emne == 'P']
    context ={
        "persons":persons,
        "courses": courses,
        "personcourses":personcourses,
        "personactivities_position":personactivities_position,
        "personactivities_project":personactivities_project,
        "personactivities":personactivities


    }
    return render(request,'app_teaching/index_load.html',context)

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

def position_activitys(request):
    all_position_activitys= models.Position_Activity.objects.all()
    return render(request,{'position_activitys': all_position_activitys})

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

def courseperson_i(request):
    all_courses_indecol =PersonCourse.objects.all()
    return render(request,'courseperson_i.html',{'coursepersons': all_courses_indecol})

def courseperson_p(request):
    all_courses_process =PersonCourse.objects.all()
    return render(request,'courseperson_p.html',{'coursepersons': all_courses_process})

def courseperson_t(request):
    all_courses_thermo=PersonCourse.objects.all()
    return render(request,'courseperson_t.html',{'coursepersons': all_courses_thermo})


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


