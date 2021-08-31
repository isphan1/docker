from django.contrib import admin
from django.urls import path,re_path,include
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve 

from .views import index

urlpatterns = [
    path('',index),
    path('api/',include('api.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^mediafiles/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^staticfiles/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

