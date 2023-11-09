from rest_framework import serializers
from .models import AgentPointModel, TaskTypeModel


class AgentPointSerializer(serializers.ModelSerializer):

    class Meta:
        model = AgentPointModel
        fields = [
            'uuid', 'address', 'agent_point_date',
            'materials', 'last_card_given',
            'approved_requests', 'last_deliver',
            'last_stimulation', 'last_teaching',
            'num_given_cards',
        ]


class TaskTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskTypeModel
        fields = [
            'uuid', 'name', 'priority',
            'work_time', 'condition_1',
            'condition_2', 'grade'
        ]

