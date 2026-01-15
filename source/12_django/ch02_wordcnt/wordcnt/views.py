from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
def wordinput(request) -> HttpResponse:
    return render(request, 'wordcnt/wordinput.html')