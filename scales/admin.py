"""
Scales admin registration.
"""
from django.contrib import admin

from .models import Score, Investigation

admin.site.register(Investigation)
admin.site.register(Score)
