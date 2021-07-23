from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns
from ytApi import views
from django.views.decorators.csrf import csrf_exempt


app_name = 'ytApi'

urlpatterns = [
    path('api/', views.get_default),
    path('api/uploadfile', csrf_exempt(views.get_pdf)),
    path('api/<qu>/', views.snippet_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)