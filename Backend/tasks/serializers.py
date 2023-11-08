from rest_framework import serializers
from tasks.models.models import Task


class CreateTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = [
            'agent_point_date', 'work_time', 'task_type', 'comment',
            'materials', 'last_card_given', 'num_given_cards', 'favorite',
            'approved_requests', 'priority', 'address', 'status', 'employee'
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
            'address', 'work_time', 'priority', 'uuid',
            'status', 'appointment_date', 'task_type',
            'employee', 'favorite', 'comment'
        ]


