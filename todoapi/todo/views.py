from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,status as s ,response
from .serializer import TodoSerializer
from .models import TodoModel
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from django.utils import timezone

class TodoViewSet(viewsets.ModelViewSet):
    queryset=TodoModel.objects.all()
    serializer_class=TodoSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        return TodoModel.objects.filter(user=self.request.user).order_by('-created_at')
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    @action(detail=True,methods=['patch'],url_path='update_status')
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
            return response.Response(serializer.data, status=s.HTTP_200_OK)

        except Exception as e:
            #return response.Response({'detail': str(e)}, status=s.HTTP_400_BAD_REQUEST)   p-'[0]
            return response.Response({'detail':str(e)},status=s.HTTP_400_BAD_REQUEST) 
    