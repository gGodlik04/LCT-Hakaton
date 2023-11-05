from rest_framework import serializers
from worker.models import Task


class CreateTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = [
            'agent_point_date', 'address',
            'materials', 'last_card_given', 'num_given_cards',
            'approved_requests', 'employee', 'priority'
        ]


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'address', 'work_time', 'priority',
            'status', 'appointment_date', 'task_type'
        ]
