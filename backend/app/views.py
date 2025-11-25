from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def call_api(request):
    return render(request, 'index.html')

def call_html(request):
    return HttpResponse('hi')