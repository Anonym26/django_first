from django.urls import path
from .views import create_user, login_user, logout_user


urlpatterns = [
    path('registration/', create_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout')
]


