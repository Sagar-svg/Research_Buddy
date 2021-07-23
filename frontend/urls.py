from django.urls import path, include
from . import views
from . import apps
app_name = apps.FrontendConfig.name
urlpatterns = [
    path('', views.index, name = "home_page"),
]