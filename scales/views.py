"""
Scale views.
"""
from django.shortcuts import render

from scales.models import Investigation


def scales_page(request):
    """
    THe view for the maing scales page.

    :param request: The HTTP request accessing the page.
    :type request: django.http.HttpRequest
    :return: The HTTP response for the view.
    :rtype: django.http.HttpResponse
    """
    investigations = Investigation.objects.all()
    return render(request, 'scales.html', {'investigations': investigations})
