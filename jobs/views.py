from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Job


def jobs(request):
    jobs = Job.objects

    return render(request, 'jobs/jobs.html',{'jobs' : jobs})
