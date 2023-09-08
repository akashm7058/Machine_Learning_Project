
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('firstapp.urls')),
    path('go',include('firstapp.urls')),
    path('go1',include('firstapp.urls')),
]

