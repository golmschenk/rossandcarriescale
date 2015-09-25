from django.shortcuts import render
from django.http import HttpResponse


def scales_page(request):
    return HttpResponse(b'<title>Ross and Carrie Scale</title>')
