from django.test import TestCase


class TestScalesView(TestCase):

    def test_front_page_has_title(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'scales.html')
