"""taxi_park URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from taxi.views import main_page, signup_manager, signup_driver

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/v1/cars/', include('taxi.urls')),
    path('api/v1/auth/', include('rest_framework.urls')),
    path('', main_page, name='main_page'),
    path('manager/', signup_manager, name='signup_manager'),
    path('driver/', signup_driver, name='signup_driver'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
