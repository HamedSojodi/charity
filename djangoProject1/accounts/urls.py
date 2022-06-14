from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import UserRegistration, LogoutAPIView

app_name = 'accounts'
urlpatterns = [
    path('login/', obtain_auth_token),
    path('logout/', LogoutAPIView.as_view()),
    path('register/', UserRegistration.as_view()),
]
