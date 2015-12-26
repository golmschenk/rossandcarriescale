"""
Scale view tests.
"""
from unittest.mock import patch, Mock

from django.test import TestCase

from scales.views import scales_page


class TestScalesView(TestCase):

    def test_front_page_has_title(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'scales.html')

    @patch('scales.views.render')
    @patch('scales.views.Investigation')
    def test_existing_investigations_are_passed_to_the_template(self, MockInvestigation, mock_render):
        mock_request = Mock()
        mock_investigations = MockInvestigation.objects.all.return_value

        scales_page(mock_request)

        mock_render.assert_called_with(mock_request, 'scales.html', {'investigations': mock_investigations})
