from django.shortcuts import render

from scales.models import Investigation


def scales_page(request):
    investigations = Investigation.objects.all()
    return render(request, 'scales.html', {'investigations': investigations})
