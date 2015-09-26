from django.shortcuts import render


def scales_page(request):
    return render(request, 'scales.html')
