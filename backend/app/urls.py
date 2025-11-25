from django.urls import path
from .views import call_api, call_html

urlpatterns = [
    path('', call_api),
    path('http', call_html)
]