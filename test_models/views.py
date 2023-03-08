from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseNotFound

'''
Create redirect 

301 страница перемещена на другой постоянный URL адрес
302 страница перемещена временно на другой URL адрес


'''


def index(request):
    return HttpResponse(f'<h1>animal page</h1>')

def categories(request, cat_id):
    return HttpResponse(f'<h1>categories page</h1><p>{cat_id}</p>')

def archive(request, year):
    print(f'---> {type(year)}')
    print(request.GET)
    if int(year)>2023:
        pageNotFound()
    if int(year)>2025:
        return redirect('/')
    return HttpResponse(f'<h1>archive page {year}</h1>')

def pageNotFound(request, exception):
    return HttpResponseNotFound(f'Error page not found')