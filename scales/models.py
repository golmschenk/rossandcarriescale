from django.db import models


class Investigation(models.Model):
    title = models.CharField(max_length=255, default='')


class Score(models.Model):
    person = models.CharField(max_length=255, default='')
    investigation = models.ForeignKey(Investigation, default=None)
