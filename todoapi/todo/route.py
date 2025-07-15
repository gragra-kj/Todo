from rest_framework.routers import DefaultRouter
from .views import TodoViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('todo', TodoViewSet, basename='todo')  # 👈 Add basename

urlpatterns = [
    path('', include(router.urls)),
]
