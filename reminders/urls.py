#include used to include other apps urls
from django.contrib import admin
from django.urls import path,re_path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', views.notes ),  #creates url for home page
    path('notes/', include('notes.urls')), #includes any urls in notes->urls.py
]
urlpatterns += staticfiles_urlpatterns()