from wsgiref.util import request_uri
from django.http import HttpResponse
from django.shortcuts import redirect, render
import accounts
from .models import Note
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
@login_required(login_url='/accounts/login/')
def notes(request):
    #return HttpResponse('Hello')
    user = request.user
    stickynotes =  Note.objects.filter(author_id = user)
    return render(request, "notes/stickynotes.html", {"stickynotes": stickynotes})

@login_required(login_url='/accounts/login/')   #->have to be loggied in to create_note so instead redirect to login
def create_note(request):
    if request.method=='POST':
        form = forms.CreateNote(request.POST)
        if form.is_valid():
            #save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            #response.user.auth.add(instance)
            return redirect('notes:sticky')
    elif request.method=='GET':
        form = forms.CreateNote()

    return render(request, 'notes/create_note.html',{'form':form})


def editNote(request,pk):
    note = Note.objects.get(id=pk)
    form = forms.CreateNote(instance=note)
    
    if request.method== 'POST':
        form = forms.CreateNote(request.POST, instance = note)
        if form.is_valid():
            form.save()
            return redirect('notes:sticky')
        
    context = {
        'form':form
    }
    return render(request, 'notes/update_note.html',context)

def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return redirect('notes:sticky')
    