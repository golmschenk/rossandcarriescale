from unittest.mock import Mock

from django.test import TestCase

from scales.models import Score, Investigation


class TestScoreModel(TestCase):

    def test_default_person(self):
        score = Score()
        self.assertEqual(score.person, '')

    def test_person_saved(self):
        Score.objects.create(person='Test Name', investigation=Investigation.objects.create())
        saved_score = Score.objects.first()
        self.assertEqual(saved_score.person, 'Test Name')

    def test_score_belongs_to_investigation(self):
        score = Score()
        investigation = Investigation.objects.create()
        score.investigation = investigation
        score.save()
        self.assertIn(score, investigation.score_set.all())

    def test_default_danger(self):
        score = Score()
        self.assertEqual(score.danger, 1)

    def test_danger_saved(self):
        Score.objects.create(danger=2, investigation=Investigation.objects.create())
        saved_score = Score.objects.first()
        self.assertEqual(saved_score.danger, 2)

    def test_default_cost(self):
        score = Score()
        self.assertEqual(score.cost, 1)

    def test_cost_saved(self):
        Score.objects.create(cost=2, investigation=Investigation.objects.create())
        saved_score = Score.objects.first()
        self.assertEqual(saved_score.cost, 2)

    def test_default_creepiness(self):
        score = Score()
        self.assertEqual(score.creepiness, 1)

    def test_creepiness_saved(self):
        Score.objects.create(creepiness=2, investigation=Investigation.objects.create())
        saved_score = Score.objects.first()
        self.assertEqual(saved_score.creepiness, 2)

    def test_default_pseudoscience(self):
        score = Score()
        self.assertEqual(score.pseudoscience, 1)

    def test_pseudoscience_saved(self):
        Score.objects.create(pseudoscience=2, investigation=Investigation.objects.create())
        saved_score = Score.objects.first()
        self.assertEqual(saved_score.pseudoscience, 2)

    def test_rating_display_shows_an_integer_as_is(self):
        display_two = Score.rating_display(2)
        display_ten = Score.rating_display(10)
        self.assertEqual(display_two, '2')
        self.assertEqual(display_ten, '10')

    def test_rating_display_rounds_float(self):
        display_number = Score.rating_display(3.1415)
        self.assertEqual(display_number, '3.14')

    def test_rating_display_removes_unnecessary_zeros_and_decimals(self):
        display_number = Score.rating_display(3.00000)
        self.assertEqual(display_number, '3')
        display_number = Score.rating_display(3.1000)
        self.assertEqual(display_number, '3.1')

    def test_pseudoscience_display_uses_formatter(self):
        score = Score(pseudoscience=2)
        score.rating_display = Mock(return_value='2')

        display_value = score.pseudoscience_display

        score.rating_display.assert_called_with(2)
        self.assertEqual(display_value, '2')

    def test_cost_display_uses_formatter(self):
        score = Score(cost=2)
        score.rating_display = Mock(return_value='2')

        display_value = score.cost_display

        score.rating_display.assert_called_with(2)
        self.assertEqual(display_value, '2')

    def test_danger_display_uses_formatter(self):
        score = Score(danger=2)
        score.rating_display = Mock(return_value='2')

        display_value = score.danger_display

        score.rating_display.assert_called_with(2)
        self.assertEqual(display_value, '2')

    def test_creepiness_display_uses_formatter(self):
        score = Score(creepiness=2)
        score.rating_display = Mock(return_value='2')

        display_value = score.creepiness_display

        score.rating_display.assert_called_with(2)
        self.assertEqual(display_value, '2')


class TestInvestigationModel(TestCase):

    def test_default_title(self):
        investigation = Investigation()
        self.assertEqual(investigation.title, '')

    def test_title_saved(self):
        Investigation.objects.create(title='Test Title')
        saved_investigation = Investigation.objects.first()
        self.assertEqual(saved_investigation.title, 'Test Title')

    def test_html_id_conversion_of_title(self):
        investigation = Investigation(title='Test Title')
        self.assertEqual(investigation.html_id, 'test_title')
