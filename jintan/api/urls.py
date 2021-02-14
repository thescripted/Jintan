from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='api-login'),
    path('logout/', views.LogoutView.as_view(), name='api-logout'),
    path('signup/', views.CreateUserView.as_view(), name='api-signup'),
    path('session/', views.SessionView.as_view(), name='api-session'),
    path('whoami/', views.WhoAmIView.as_view(), name='api-whoami'),
    path('api-token-auth/', obtain_auth_token),  # log-in service & token revalidation
]
