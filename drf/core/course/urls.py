from django.urls import path
from core.course import views

urlpatterns = [
    path('', views.get_courses),
    path('categories/', views.get_categories),
    path('<slug:course_slug>', views.get_course),
    path('<slug:course_slug>/<slug:lesson_slug>', views.add_comment, name='add-comment'),
    path('<slug:course_slug>/<slug:lesson_slug>/comments', views.get_comments, name='get-comments')
]