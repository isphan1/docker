from django.urls import path
from .views import NewsApi

urlpatterns = [
    path('news/',NewsApi.as_view()),
]
