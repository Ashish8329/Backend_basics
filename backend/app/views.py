from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def call_api(request):
    return render(request, 'index.html')

def call_html(request):
    return HttpResponse('hi')

@method_decorator(csrf_exempt, name='dispatch')
class ApiView(View):
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