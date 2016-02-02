"""
Scale app model classes.
"""
from django.db import models


class Investigation(models.Model):
    """
    The model to store data about investigations.
    """
    title = models.CharField(max_length=255, default='')

    @property
    def html_id(self):
        """
        The HTML ID to be assigned to the div for the investigation.

        :return: The HTML ID for the investigation.
        :rtype: str
        """
        return self.title.replace(' ', '_').lower()


class Score(models.Model):
    """
    The model to store the score data.
    """
    person = models.CharField(max_length=255, default='')
    investigation = models.ForeignKey(Investigation, default=None)
    danger = models.DecimalField(max_digits=6, decimal_places=4, default=1)
    cost = models.DecimalField(max_digits=6, decimal_places=4, default=1)
    creepiness = models.DecimalField(max_digits=6, decimal_places=4, default=1)
    pseudoscience = models.DecimalField(max_digits=6, decimal_places=4, default=1)

    @staticmethod
    def rating_display(number):
        """
        Returns a display version of the score's value.

        :param number: The number to make presentable.
        :type number: Decimal
        :return: The presentation number.
        :rtype: str
        """
        return str("{0:.2f}".format(number).rstrip('0').rstrip('.'))

    @property
    def pseudoscience_display(self):
        """
        The pseudoscince score in a presentable version.

        :return: The presentation number.
        :rtype: str
        """
        return self.rating_display(self.pseudoscience)

    @property
    def cost_display(self):
        """
        The cost score in a presentable version.

        :return: The presentation number.
        :rtype: str
        """
        return self.rating_display(self.cost)

    @property
    def danger_display(self):
        """
        The danger score in a presentable version.

        :return: The presentation number.
        :rtype: str
        """
        return self.rating_display(self.danger)

    @property
    def creepiness_display(self):
        """
        The creepiness score in a presentable version.

        :return: The presentation number.
        :rtype: str
        """
        return self.rating_display(self.creepiness)
