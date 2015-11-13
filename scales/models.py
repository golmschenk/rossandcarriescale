from django.db import models


class Investigation(models.Model):
    title = models.CharField(max_length=255, default='')

    @property
    def html_id(self):
        return self.title.replace(' ', '_').lower()


class Score(models.Model):
    person = models.CharField(max_length=255, default='')
    investigation = models.ForeignKey(Investigation, default=None)
    danger = models.DecimalField(max_digits=6, decimal_places=4, default=1)
    cost = models.DecimalField(max_digits=6, decimal_places=4, default=1)
    creepiness = models.DecimalField(max_digits=6, decimal_places=4, default=1)
    pseudoscience = models.DecimalField(max_digits=6, decimal_places=4, default=1)

    @staticmethod
    def rating_display(number):
        return str("{0:.2f}".format(number).rstrip('0').rstrip('.'))

    @property
    def pseudoscience_display(self):
        return self.rating_display(self.pseudoscience)

    @property
    def cost_display(self):
        return self.rating_display(self.cost)

    @property
    def danger_display(self):
        return self.rating_display(self.danger)

    @property
    def creepiness_display(self):
        return self.rating_display(self.creepiness)
