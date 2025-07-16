from rest_framework import serializers
from .models import TodoModel

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='todo-detail')

    class Meta:
        model = TodoModel
        fields = ['url', 'id', 'title', 'description', 'status', 'completed_at', 'created_at']

    def validate(self, data):
        status = data.get('status', self.instance.status if self.instance else None)
        completed_at = data.get('completed_at', self.instance.completed_at if self.instance else None)

        if status in ['PENDING', 'IN_PROGRESS'] and completed_at:
            raise serializers.ValidationError({
                "completed_at": "You cannot set 'completed_at' unless the task is marked as COMPLETED."
            })

        return data
