from rest_framework import serializers

from .models import Course


'''
When we are querying database we cannot directly render the objects returned in the views.
It is necessary to serialize the queried object to transform it in a JSON object
that can be handled by the view and rendered out.
'''

class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('cr_id', 'cr_title', 'cr_slug', 'cr_short', 'cr_long')