from django.test import TestCase
from scales.models import Score, Investigation


class TestScoreModel(TestCase):

    def test_default_person(self):
        score = Score()
        self.assertEqual(score.person, '')

    def test_score_belongs_to_investigation(self):
        score = Score()
        investigation = Investigation.objects.create()
        score.investigation = investigation
        score.save()
        self.assertIn(score, investigation.score_set.all())
