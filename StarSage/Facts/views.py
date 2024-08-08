from django.shortcuts import render
from django.http import HttpResponse

def home_facts(request):
    return render(request, 'home_facts.html')


