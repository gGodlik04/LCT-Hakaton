from rest_framework import serializers
from tasks.models import Task

from directories.serializers import TaskTypeSerializer, AgentPointSerializer
from accounts.serializers import UserSerializer


class ChartSerializer(serializers.ModelSerializer):
    agent_point = serializers.ReadOnlyField(source='AgentPoint.address')
    task_type = serializers.ReadOnlyField(source='task_type.name')
    employee = serializers.ReadOnlyField(source='accounts_user.last_name')

    class Meta:
        model = Task
        fields = [
            'priority', 'agent_point', 'task_type',
            'status', 'appointment_date', 'employee',
            'favorite', 'comment',

        ]
