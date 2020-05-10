"""simplesocial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views   # import views from the current directory one

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomePage.as_view(), name='home'),  # home-page i.e. HomePage representing 'index.html'
    url(r'^accounts/', include('accounts.urls', namespace='accounts')), # connecting accounts namespace of accounts.url to account's application
    url(r'^accounts/', include('django.contrib.auth.urls')), # adding auth to our project; allows everything to connect with auth
    url(r'^test/$', views.TestPage.as_view(), name='test'),
    url(r'^thanks/$', views.ThanksPage.as_view(), name='thanks'),
    url(r'^posts/', include('posts.urls', namespace='posts')),# Added both of these down below, in order to get rid of the error "NoReverseMatch at /", 'groups' is not a registered namespace
    url(r'^groups/', include('groups.urls', namespace='groups')), # Added both of these down below, in order to get rid of the error "NoReverseMatch at /", 'groups' is not a registered namespace
]
