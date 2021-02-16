"""jintan URL Configuration

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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin Services
    path('auth/', include('rest_framework.urls')),  # (TESTING) Auth Services

    path('api/', include('api.urls')),  # API Services
    path('account/', include('rest_auth.urls')),  # Login/Logout
    path('account/registration', include('rest_auth.registration.urls')),  # Registration
    path('stripe/', include('djstripe.urls', namespace='djstripe')),
]
