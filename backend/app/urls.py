from django.urls import path
from .views import call_api, call_html, ApiViews, API_withView
from rest_framework import routers

router = routers.DefaultRouter()


urlpatterns = [
    path('', call_api),
    path('http/', call_html),
    path('view/', ApiViews.as_view()),
    path('apiview/',API_withView.as_view() )
]