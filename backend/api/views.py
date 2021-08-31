from .serializers import NewsSerializer
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from news.models import News

# Create your views here.

class NewsApi(ListAPIView):

    serializer_class = NewsSerializer
    queryset = News.objects.all()
