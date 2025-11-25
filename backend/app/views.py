from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination 
import requests
from .decorator import add_pagination
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def call_api(request):
    return render(request, 'index.html')

def call_html(request):
    return HttpResponse('hi')

@method_decorator(csrf_exempt, name='dispatch')
class ApiViews(View):

    def get(self, request):
        return HttpResponse('woring view')
    
    def post(self, request):

        import json
        body_decode = request.body.decode('utf-8')

        try:
            
            body = json.loads(request.body) if body_decode else {}
        except json.JSONDecodeError:
            body = {"error":"error"}
        return JsonResponse({"data":body})
    
class API_withView(APIView):

    def get(self, request):
        return Response(status=200, data="done")

    def post(self, request):
        return Response(status=202, data='created')


class ClassBasedViewset(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    
    @add_pagination
    def list(self, request):

        url = "https://jsonplaceholder.typicode.com/posts"
        external_response = requests.get(url)
        data = external_response.json() # This is a Python list

        
        return Response(status=200, data=data)
    
    def retrieve(self, request, pk):
        return Response(status=200, data='working retrieve')
    
    def create(self, request):
        return Response(status=200, data='working create')
    
    def destroy(self, request, pk):
        return Response(status=200, data='working destroy')
    

    def update(self, request, pk):
        return Response(status=200, data='working update')
    
    def partial_update(self, request, pk):
        return Response(status=200, data='working partial_update')
