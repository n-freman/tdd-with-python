from django.urls import path
from django.contrib.auth.views import LogoutView

from accounts.views import send_login_email, login


urlpatterns = [
    path('send_login_email', send_login_email, name='send_login_email'),
    path('login', login, name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]

