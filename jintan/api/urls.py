from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('todo/', views.TodoListView.as_view(), name='api-todo'),
    # path('todo/<str:username>/', views.UserTodoListView.as_view(), name='api-user-todo-view'),
    path('todo/<int:pk>/', views.TodoDetailView.as_view(), name='api-todo-detail'),

    path('user/', views.UserListView.as_view(), name='api-user'),
    path('user/<str:username>/', views.UserDetailView.as_view(), name='api-user-detail'),
    path('profile/', views.ProfileView.as_view(), name='api-profile'),
]
