from rest_framework import serializers
from .models import TodoModel

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=TodoModel
        fields=['id','name','description','status','created_on','due_date']