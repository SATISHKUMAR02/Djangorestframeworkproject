from django.shortcuts import render
from django.http import HttpResponse

def students(request):
    data=[{
        'id':'1',
        'name':'satish',
        'age':25
    }]
    return HttpResponse(data)