"""
Functional tests for checking a basic visitor can interact with the site.
"""
from functional_tests.base import BaseFunctionalTest
from scales.models import Investigation, Score


class TestVisitor(BaseFunctionalTest):

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

        # She sees a score for both Ross and Carrie for an investigation.
        headers = self.browser.find_elements_by_tag_name('h2')
        self.assertIn(investigation1.title, [header.text for header in headers])
        investigation1_div = self.browser.find_element_by_id('pumpkin_cat_scrying')
        self.assertIn('Ross', investigation1_div.text)
        self.assertIn('Carrie', investigation1_div.text)
        self.assertIn('8', investigation1_div.text)
        self.assertIn('3', investigation1_div.text)
        self.assertIn('1', investigation1_div.text)
        self.assertIn('2', investigation1_div.text)
        self.assertIn('7', investigation1_div.text)
        self.assertIn('4', investigation1_div.text)

        # Kara also sees a second investigation with a score from both Ross and Carrie.
        headers = self.browser.find_elements_by_tag_name('h2')
        self.assertIn(investigation1.title, [header.text for header in headers])
        investigation1_div = self.browser.find_element_by_id('battery_healing')
        self.assertIn('Ross', investigation1_div.text)
        self.assertIn('Carrie', investigation1_div.text)
        self.assertIn('7', investigation1_div.text)
        self.assertIn('6', investigation1_div.text)
        self.assertIn('3', investigation1_div.text)
        self.assertIn('7.5', investigation1_div.text)
        self.assertIn('5', investigation1_div.text)

        # Interested, Kara leaves to go listen to one of the episodes.
