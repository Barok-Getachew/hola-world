from django.shortcuts import render
from django.views.generic import TemplateView

class Homepage (TemplateView) :
    template_name = 'hola.html'
class AboutPage (TemplateView) :
    template_name = 'two.html'