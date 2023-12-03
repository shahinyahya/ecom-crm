from django.test import TestCase
from django.urls import reverse

class HomePageTest(TestCase):

    def test_get(self):
        response = self.client.get(reverse('home'))
        # print(response.status_code)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html') 
