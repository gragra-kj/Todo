from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from rest_framework import viewsets, status as s, response
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from .models import TodoModel
from .serializer import TodoSerializer
from .permission import IsOwner


# Renders the HTML frontend
def todo_frontend_view(request):
    return render(request, 'todo/frontend.html')


# Handles all CRUD operations for Todo tasks
class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwner]

    def get_queryset(self):
        user = self.request.user
        if not user or not user.is_authenticated:
            return TodoModel.objects.none()
        return TodoModel.objects.filter(user=user).order_by('-created_at')


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # PATCH endpoint to update task status
    @action(detail=True, methods=['patch'], url_path='update_status')
    def update_status(self, request, pk=None):
        try:
            task = self.get_object()
            status = request.data.get('status')

            if status not in ['PENDING', 'IN_PROGRESS', 'COMPLETED']:
                raise Exception("Invalid status value")

            if status == 'COMPLETED':
                if task.status != 'COMPLETED':
                    task.status = 'COMPLETED'
                    task.completed_at = timezone.now()
                else:
                    raise Exception("Task is already marked as completed")

            elif status in ['PENDING', 'IN_PROGRESS']:
                task.status = status
                task.completed_at = None

            task.save()
            serializer = self.get_serializer(task)
            return Response(serializer.data, status=s.HTTP_200_OK)

        except Exception as e:
            return Response({'detail': str(e)}, status=s.HTTP_400_BAD_REQUEST)


