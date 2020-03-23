from django.http import HttpResponse
from django.shortcuts import render
from . import counting

def home(request):
    return render(request, 'home.html')

def count(request):
    para = request.POST['para']
    words = para.split()
    freq = counting.counti(para)
    return render(request, 'counter.html', {'para' : para, 'words' : len(words), 'freq' : freq})

