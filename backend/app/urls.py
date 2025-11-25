from django.urls import path
from .views import call_api, call_html, ApiView

urlpatterns = [
    path('', call_api),
    path('http', call_html),
    path('view', ApiView.as_view())
]