from django.db import models


class Investigation(models.Model):
    pass


class Score(models.Model):
    person = ''
    investigation = models.ForeignKey(Investigation, default=None)
