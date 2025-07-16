from django.contrib import admin
from django.urls import path, include
from todo import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/todo/', include('todo.route')),
    path('api-auth/', include('rest_framework.urls')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('todo-frontend/', views.todo_frontend_view, name='todo-frontend'),
]
