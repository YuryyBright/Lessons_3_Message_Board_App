from django.test import TestCase
from .models import Posts
from django.urls import reverse
# Create your tests here.

class PostModelTest(TestCase):
    def set_up(self):
        Posts.objects.create(text='just a text')

    def test_text_content(self):
        post = Posts.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name,'just a text')

class HomePageViewTest(TestCase):

    def set_up(self):
        Posts.objects.create(text='this is another test')


    def test_view_url_exists_at_proper_locatiuon(self):
        resp = self.cloent.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')