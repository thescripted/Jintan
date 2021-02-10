from django.urls import path, include
from .views import account_view

urlpatterns = [
    path('^', account_view),
]
