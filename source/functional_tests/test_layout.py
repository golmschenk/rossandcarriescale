from functional_tests.base import BaseFunctionalTest
from scales.models import Investigation, Score


class TestLayout(BaseFunctionalTest):

    def test_basic_style_is_loaded(self):
        # -- Setup a score to display.
        investigation1 = Investigation.objects.create(title='Pumpkin Cat Scrying')
        score1 = Score.objects.create(investigation=investigation1, person='Ross', pseudoscience=8, creepiness=3,
                                      cost=1, danger=2)
        score2 = Score.objects.create(investigation=investigation1, person='Carrie', pseudoscience=7, creepiness=4,
                                      cost=2, danger=2)

        # Kara goes to the scales app.
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # She notices that an investigation div is centered, but does not span the screen
        investigation_div = self.browser.find_element_by_id('pumpkin_cat_scrying')
        self.assertAlmostEqual(
            investigation_div.location['x'] + investigation_div.size['width'] / 2,
            512,
            delta=5
        )
        self.assertLess(investigation_div.size['width'], 950)
