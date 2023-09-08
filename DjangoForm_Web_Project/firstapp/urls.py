
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name='home page'),
    path('go',views.result,name='view page'),
    path('go1',views.show,name='view page'),
    
    
]
