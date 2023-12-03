from django.test import TestCase
from django.urls import reverse

class FormTest(TestCase):

    def get_test(self):
        response = self.client.get(reverse('create-lead'))
        print(response.status_code)