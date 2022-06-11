from django.urls import path

from .views import about_us
from . import views
urlpatterns = [

    path('', views.about_us.as_view(), name='about_us'),
]
