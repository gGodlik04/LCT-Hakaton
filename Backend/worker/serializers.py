from rest_framework import serializers
from worker.models import Task, Employee


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        field = (
            'uuid', 'task_id', 'agent_point_date',
            'materials', 'last_card_given', 'num_given_cards',
            'approved_requests', 'employee', 'priority', 'slug'
        )

