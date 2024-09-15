from django.urls import path

from django.http import HttpResponse

def hello(request):
    return HttpResponse('hello i am dinsh : ')
urlpatterns = [
    path('', hello), 
    
]