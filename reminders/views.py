from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import user_logged_in
def notes(request):
    #return HttpResponse('Hello')
    return render(request, "home.html")