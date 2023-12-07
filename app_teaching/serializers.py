# project/serializers.py
from rest_framework import serializers
from . models import Course,Position_Activity,Person,PersonCourse,PersonActivity


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("__all__")

class Position_ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Position_Activity
        fields = ("__all__")

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ("__all__")

class PersonCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonCourse
        fields = ("__all__")

class PersonActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonActivity
        fields = ("__all__")

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("__all__")