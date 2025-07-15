from rest_framework import serializers
from .models import TodoModel

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=TodoModel
        fields=['id','title','description','status','created_at','due_date']