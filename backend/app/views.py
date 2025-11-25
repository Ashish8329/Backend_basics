from django.shortcuts import render

# Create your views here.
def call_api(request):
    return render(request, 'index.html')