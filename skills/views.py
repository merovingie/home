from django.shortcuts import render
from . import views

def skills(request):

    return render(request, 'skills/skills.html')