from django.shortcuts import render
from django.http import HttpResponse

def myView(request):
    return HttpResponse('hello ahhh i m biruk what is going on?')
def todo(request):
    return render(request, 'too.html')

