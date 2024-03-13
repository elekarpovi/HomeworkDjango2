from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string


# Create your views here.
def hw(request):
    with open('myapp/templates/hw.html', 'r', encoding='utf-8') as file:
        result = file.read()
    return HttpResponse(result)



