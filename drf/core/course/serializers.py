from rest_framework import serializers

from .models import Comment, Course, Lesson, Comment


'''
When we are querying database we cannot directly render the objects returned in the views.
It is necessary to serialize the queried object to transform it in a JSON object
that can be handled by the view and rendered out.
'''

class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('cr_id', 'cr_title', 'cr_slug', 'cr_short', 'cr_long')


class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('ls_id', 'ls_title', 'ls_slug', 'ls_short', 'ls_long')


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('cm_id', 'cm_title', 'cm_content', 'cm_created_at')