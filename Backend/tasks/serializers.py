from rest_framework import serializers
from tasks.models.tasks import Task


class CreateTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = [
            'priority', 'uuid', 'agent_point',
            'status', 'appointment_date', 'task_type',
            'employee',  'comment'
        ]

        def create(self, validated_data):
            task = Task.objects.create(**validated_data)
            return task

        def update(self, validated_data):
            task = Task.objects.update(**validated_data)
            return task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'priority', 'uuid', 'agent_point',
            'status', 'appointment_date', 'task_type',
            'employee', 'favorite', 'comment'
        ]


