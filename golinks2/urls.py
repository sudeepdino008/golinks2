"""golinks2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, re_path, include, reverse_lazy
from django.views.generic import RedirectView

urlpatterns = [
    path('admin', RedirectView.as_view(url = '/admin/')),
    path('admin/', admin.site.urls),
    path('accounts/login', RedirectView.as_view(url = reverse_lazy('login_url'))),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login_url'),
    path('', include('bookmarks.urls'))
]
