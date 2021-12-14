from model_bakery import baker # delegate field creation

from django.contrib.auth.models import User
from django.urls import reverse, resolve

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from core.course.models import Category, Comment, Course, Lesson
from core.course.views import add_comment

# docker-compose exec edusys_api bash
# run test: python manage.py test core

# WARNING: each test must start with 'test' to be visible

class SignupTests(APITestCase):

    def test_signup(self):
        data = {'username': 'test1@testcase.eu', 'password': 'pwd_12345'}
        response = self.client.post('/api/v1/users/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)



class CategoryTests(APITestCase):

    def test_course_has_categories(self):
        course = baker.make(Course)
        category1 = baker.make(Category)
        category2 = baker.make(Category)
        course.cr_categ.set([category1.ct_id, category2.ct_id])
        self.assertEqual(course.cr_categ.count(), 2) # 3 => AssertionError: 2 != 3

    def test_category_has_courses(self):
        course = baker.make(Course)
        category1 = baker.make(Category)
        category2 = baker.make(Category)
        category1.courses.add(course)
        category2.courses.add(course)
        self.assertEqual(course.cr_categ.count(), 2) 

    def test_category_model_str(self):
        category = Category.objects.create(ct_title='Programming')
        self.assertEqual(str(category), 'Programming')



class CourseTests(APITestCase):

    def setUp(self):
        self.course = baker.make(Course, cr_title = 'New Test Course', cr_slug='new-test-course')
        self.user = User.objects.create_user(username='test2@testcase.eu', password='apassword')

    def test_get_courses(self):
        response = self.client.get('/api/v1/courses/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_course_unauth(self):
        response = self.client.get('/api/v1/courses/new-test-course')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_course(self):
        self.client.force_authenticate(user=self.user) # directly authenticate the request for testing
        response = self.client.get('/api/v1/courses/', kwargs={'cr_slug':'new-test-course'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response,'cr_title')



class CommentTests(APITestCase):

    def setUp(self):
        self.lesson = baker.make(Lesson)
        self.course = baker.make(Course)
        self.user = User.objects.create_user(username='test3@testcase.eu', password='apassword')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication() # token authentication 

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key) # token header

    def test_add_comment(self):
        #add_url = reverse('add-comment', kwargs={'course_slug': self.course.cr_slug, 'lesson_slug':self.lesson.ls_slug})
        add_url = reverse('add-comment', args=[self.course.cr_slug, self.lesson.ls_slug])
        response = self.client.post(add_url, {'title':'a title', 'content':'a content'}) # data.get('title') required

        print(resolve(add_url)) # ResolverMatch
        self.assertEqual(resolve(add_url).func, add_comment) # check url resolve and call function
        self.assertEqual(Comment.objects.count(), 1) # check if an instance is created in the database
        self.assertEqual(response.status_code, status.HTTP_200_OK) # check response status

    def test_get_comments(self):
        response = self.client.get(reverse('get-comments', args=[self.course.cr_slug, self.lesson.ls_slug]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_comments_unauth(self):
        self.client.force_authenticate(user=None) # unauthenticate user
        response = self.client.get(reverse('get-comments', args=[self.course.cr_slug, self.lesson.ls_slug]))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
