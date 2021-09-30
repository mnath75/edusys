from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Course
from .serializers import CourseListSerializer, LessonListSerializer


@api_view(['GET'])
def get_courses(request):
    courses=Course.objects.all()
    serializer=CourseListSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_course(request, course_slug):
    course=Course.objects.get(cr_slug = course_slug)
    course_serializer=CourseListSerializer(course)
    lesson_serializer=LessonListSerializer(course.lessons.all(), many=True)

    data = {
        'course': course_serializer.data,
        'lessons': lesson_serializer.data
    }
    return Response(data)