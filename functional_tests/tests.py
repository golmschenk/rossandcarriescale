from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from scales.models import Investigation, Score


class TestVisitor(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_visitor_sees_scale_scores(self):
        # -- Setup a few scores to display.
        investigation1 = Investigation.objects.create(title='Pumpkin Cat Scrying')
        score1 = Score.objects.create(investigation=investigation1, person='Ross', pseudoscience=8, creepiness=3,
                                      cost=1, danger=2)
        score2 = Score.objects.create(investigation=investigation1, person='Carrie', pseudoscience=7, creepiness=4,
                                      cost=2, danger=2)
        investigation2 = Investigation.objects.create(title='Battery Healing')
        score3 = Score.objects.create(investigation=investigation2, person='Ross', pseudoscience=7, creepiness=6,
                                      cost=3, danger=6)
        score4 = Score.objects.create(investigation=investigation2, person='Carrie', pseudoscience=7.5, creepiness=5,
                                      cost=5, danger=7)

        # Kara goes to the Ross and Carrie Scale app.
        self.browser.get(self.live_server_url)

        # Kara sees the title of the page add guesses she has the right link.
        self.assertEqual(self.browser.title, "Ross and Carrie Scale")
        self.fail('Finish the test!')

        # She sees a score for both Ross and Carrie for an investigation.

        # Kara also sees a second investigation with a score from both Ross and Carrie.

        # Interested, Kara leaves to go listen to one of the episodes.
