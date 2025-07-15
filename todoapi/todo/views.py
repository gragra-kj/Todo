from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializer import TodoSerializer
from .models import TodoModel
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class TodoViewSet(viewsets.ModelViewSet):
    queryset=TodoModel.objects.all()
    serializer_class=TodoSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        return TodoModel.objects.filter(user=self.request.user).order_by('-created_at')
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    