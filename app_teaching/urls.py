from django.urls import path
from . import views
from app_teaching.views import BootstrapFilterView

urlpatterns = [
    path('', views.index, name = 'index'),
    path('plot/',views.plot,name ='plot'),
    path('about', views.about, name = 'about'),
    path('admin', views.admin, name = 'admin'),
    path('courses/', views.courses, name = 'courses'),
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
