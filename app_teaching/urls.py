from django.urls import path
from . import views
# from app_teaching.views import BootstrapFilterView

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about', views.about, name = 'about'),
    path('admin', views.admin, name = 'admin'),
    path('courses/', views.courses, name = 'courses'),
    path('persons/', views.persons, name = 'persons'),
    path('course/<str:pk>', views.CourseDetailView.as_view(), name = 'course_details'),
    path('person/<str:pk>', views.PersonDetailView.as_view(), name = 'person_details'),

    # path('bootstrap/',BootstrapFilterView,name = 'bootstrap_form')
]
