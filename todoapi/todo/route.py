from rest_framework.routers import DefaultRouter
from .views import TodoViewSet,todo_frontend_view
from django.urls import path, include

router = DefaultRouter()
router.register('todo', TodoViewSet, basename='todo')  

urlpatterns = [
    path('', include(router.urls)),
    #path('todo-frontend/', todo_frontend_view, name='todo-frontend'),
]
