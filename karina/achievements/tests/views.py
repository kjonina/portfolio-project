from django.test import TestCase, Client
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from achievements.views import achievements


class TestViews(TestCase):

    def setUp(self):
        self.client =  Client()
        self.achievements_url = reverse('achievements')


    def test_thesis_GET(self):
        response = self.client.get(self.achievements_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'achievements/home.html')
