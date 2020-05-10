from django.conf.urls import url
''' Django 1.11 has introduced LoginView and LogoutView so that we dont have to take care of it in our views.py file '''
from django.contrib.auth import views as auth_views
''' my own views.py file '''
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'logout/$', auth_views.LogoutView.as_view(), name='logout'), # default view in logout
    url(r'signup/$', views.SignUp.as_view(),name='signup')
]