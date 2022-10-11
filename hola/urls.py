from django.urls import path
from hola.views import * 

urlpatterns = [
    path('home/', Homepage.as_view(),name='Home'),
    path('About/',AboutPage.as_view(), name='About')
]