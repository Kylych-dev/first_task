from django.urls import path, re_path
from .views import index, archive, categories


urlpatterns = [
    path('', index),
    path('cat/<int:cat_id>', categories),
    re_path(r'arc/(?P<year>[0-9]{4})', archive)
]




'''
path("cats/<int:catid/>/", categories)
re_path тоже самое только с использованием регулярных выражений 

str - любая не пустая строка, исключая символ "/"
int - любое положительное целое число, включая ()
slug - слаг, то есть, латиница ASCII таблицы, символы дефисы и подчеркивания 
uuid - цифры, малые латинские символы ASCII, дефис 
path - любая не пустая строка, включая символ "/"
'''