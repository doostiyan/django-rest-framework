from django.urls import path
from rest_framework.authtoken import views as auth_token

from accounts import views
app_name = 'accounts'
urlpatterns = [
    path('register/', views.UserRegister.as_view(), name='user_register'),
    path('api-token-auth/', auth_token.obtain_auth_token, )
]