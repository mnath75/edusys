from django.urls import path
from core.course import views

urlpatterns = [
    path('', views.get_courses),
    path('<slug:course_slug>', views.get_course)
]