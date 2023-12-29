
from django.urls import path, include
from .views import  login_user

urlpatterns = [
    path("login_user",login_user, name='login'),
    path("memberv/", include('django.contrib.auth.urls')),
    path("members/", include('members.urls'))
]
