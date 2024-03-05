from django.urls import path
from . import views

urlpatterns = [

    path('1/',views.home,name='home'),
    path('',views.index,name='index.html'),
]