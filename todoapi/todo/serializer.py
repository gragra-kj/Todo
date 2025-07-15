from rest_framework import serializers
from .models import TodoModel

class TodoSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = TodoModel
        fields = ['url', 'id', 'title', 'description', 'status', 'due_date', 'completed_at']
        extra_kwargs = {
            'url': {'view_name': 'todo-detail', 'lookup_field': 'pk'}
        }