from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Course, Lesson, Comment, Category
from .serializers import CourseListSerializer, LessonListSerializer, CommentListSerializer, CategoryListSerializer

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_categories(request):
    categories=Category.objects.all()
    serializer=CategoryListSerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_courses(request):
    filters = {}
    category = request.GET.get('category_id')
    if category:
        filters['cr_categ'] = category
    courses=Course.objects.filter(**filters)
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

@api_view(['POST'])
def add_comment(request, course_slug, lesson_slug):
    data = request.data
    title = data.get('title')
    content = data.get('content')

    lesson = Lesson.objects.get(ls_slug= lesson_slug)

    comment = Comment.objects.create(
        cm_lesson=lesson,
        cm_title=title,
        cm_content=content,
        cm_created_by=request.user)

    return Response({'message':'comment added in db'})


@api_view(['GET'])
def get_comments(request, course_slug, lesson_slug):
    lesson = Lesson.objects.get(ls_slug= lesson_slug)
    comments=lesson.comments.all()
    serializer=CommentListSerializer(comments, many=True)
    return Response(serializer.data)