from rest_framework import serializers
from todo.models import Todo
 
 
class TodoSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Tutorial
        fields = ('id',
                  'task',
                  'date',
                  'is_complete',
                  'description')