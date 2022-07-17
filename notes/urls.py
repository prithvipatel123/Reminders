from django.contrib import admin
from django.urls import path,re_path
from . import views

app_name = "notes"
urlpatterns = [
    path('', views.notes, name="sticky"),  #creates url for home page
    path('create/',views.create_note, name= "create" ),
    path('update/<int:pk>/',views.editNote, name= "edit"),
    path('delete/<int:pk>/',views.deleteNote, name= "delete"),
]
