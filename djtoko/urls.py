"""djtoko URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('admin/', include('admintoko.urls')),
    path('', views.index, name='home'),
    path('get_data', views.get_data),
    path('get_api', views.get_api),
    re_path(r'^produk/$', views.produk, name='produk'),
    re_path(r'^produk/(?P<produk_id>\w+)$', views.produk, name='produk'),
    re_path(r'^beli/$', views.beli, name='beli'),
    re_path(r'^beli/(?P<produk_id>\w+)$', views.beli, name='beli')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)