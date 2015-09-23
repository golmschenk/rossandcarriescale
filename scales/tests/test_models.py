from django.test import TestCase
from scales.models import Score, Investigation


class TestScoreModel(TestCase):

    def test_default_person(self):
        score = Score()
        self.assertEqual(score.person, '')

    def test_person_saved(self):
        Score.objects.create(title='Test Name')
        saved_score = Score.objects.first()
        self.assertEqual(saved_score.title, 'Test Name')

    def test_score_belongs_to_investigation(self):
        score = Score()
        investigation = Investigation.objects.create()
        score.investigation = investigation
        score.save()
        self.assertIn(score, investigation.score_set.all())


class TestInvestigationModel(TestCase):

    def test_default_title(self):
        investigation = Investigation()
        self.assertEqual(investigation.title, '')

    def test_title_saved(self):
        Investigation.objects.create(title='Test Title')
        saved_investigation = Investigation.objects.first()
        self.assertEqual(saved_investigation.title, 'Test Title')
