from django.urls import path
from . import views
from app_teaching.views import BootstrapFilterView

urlpatterns = [
    path('', views.index, name = 'index'),
    path('plot/',views.plot,name ='plot'),
    path('index_load/', views.load,name ='index_load'),
    
    # path('plot/index_load/index_nb_stud_type', views.nb_student,name ='nb_student'),
    # path('plot/index_load/teaching_indecol',views.indecol,name ='teaching_indecol'),
    # path('plot/index_load/teaching_thermo',views.thermo,name ='teaching_thermo'),
    # path('plot/index_load/teaching_power',views.power,name ='teaching_power'),
    # path('plot/index_load/teaching_ses',views.ses,name ='teaching_ses'),
    
    path('index_nb_stud_type/', views.nb_student,name ='index_nb_stud_type'),
    # path('plot/index_nb_stud_type/index_load', views.load,name ='index_load'),
    # path('plot/index_nb_stud_type/teaching_indecol', views.indecol,name ='teaching_indecol'),
    # path('plot/index_nb_stud_type/teaching_thermo',views.thermo,name ='teaching_thermo'),
    # path('plot/index_nb_stud_type/teaching_power',views.power,name ='teaching_power'),
    # path('plot/index_nb_stud_type/teaching_ses',views.ses,name ='teaching_ses'),

    path('teaching_indecol/',views.indecol,name ='teaching_indecol'),
    path('teaching_ses/',views.ses,name ='teaching_ses'),
    path('teaching_power/',views.power,name ='teaching_power'),
    path('teaching_thermo/',views.thermo,name ='teaching_thermo'),


    # path('plot/teaching_indecol/index_load', views.load,name ='index_load'),
    # path('plot/teaching_indecol/teaching_thermo',views.thermo,name ='teaching_thermo'),
    # path('plot/teaching_indecol/teaching_power',views.power,name ='teaching_power'),
    # path('plot/teaching_indecol/teaching_ses',views.ses,name ='teaching_ses'),

    # path('plot/teaching_thermo/index_load', views.load,name ='index_load'),
    # path('plot/teaching_thermo/teaching_indecol', views.indecol,name ='teaching_indecol'),
    # path('plot/teaching_thermo/teaching_power',views.power,name ='teaching_power'),
    # path('plot/teaching_thermo/teaching_ses',views.ses,name ='teaching_ses'),

    # path('plot/teaching_ses/index_load', views.load,name ='index_load'),
    # path('plot/teaching_ses/teaching_indecol', views.indecol,name ='teaching_indecol'),
    # path('plot/teaching_ses/teaching_thermo',views.power,name ='teaching_power'),
    # path('plot/teaching_ses/teaching_power',views.ses,name ='teaching_ses'),
    
    # path('plot/teaching_power/index_load', views.load,name ='index_load'),
    # path('plot/teaching_power/teaching_indecol', views.indecol,name ='teaching_indecol'),
    # path('plot/teaching_power/teaching_thermo',views.power,name ='teaching_power'),
    # path('plot/teaching_power/teaching_ses',views.ses,name ='teaching_ses'),


    path('about', views.about, name = 'about'),
    path('admin/', views.admin, name = 'admin'),
    path('courses/', views.courses, name = 'courses'),
    # path('position_activitys/', views.position_activitys, name = 'position_activitys'),

    path('courseperson', views.courseperson, name = 'courseperson'),
    path('courseperson_s/', views.courseperson_s, name = 'courseperson_s'),
    path('courseperson_i/', views.courseperson_i, name = 'courseperson_i'),
    path('courseperson_p/', views.courseperson_p, name = 'courseperson_p'),
    path('courseperson_t/', views.courseperson_t, name = 'courseperson_t'),

    path('courses_ses/', views.courses_ses, name = 'courses_ses'),
    path('courses_indecol/', views.courses_indecol, name = 'courses_indecol'),
    path('courses_process/', views.courses_process, name = 'courses_process'),
    path('courses_thermo/', views.courses_thermo, name = 'courses_thermo'),
    path('persons/', views.persons, name = 'persons'),

    path('course/<str:pk>', views.CourseDetailView.as_view(), name = 'course_details'),
    path('person/<str:pk>', views.PersonDetailView.as_view(), name = 'person_details'),

    path('bootstrap/',BootstrapFilterView,name = 'bootstrap_form')
]
