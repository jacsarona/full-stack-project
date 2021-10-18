from django.shortcuts import render
from django.http import HttpResponse
 
# Create your views here.
def index(request):
    return render(request, 'myapp/main.html')

def my_name(request):
    context = {'name': 'James Angelo C. Sarona'}
    return render(request, 'myapp/myapp.html', context)