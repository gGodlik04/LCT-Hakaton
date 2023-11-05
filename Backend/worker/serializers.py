from rest_framework import serializers
from worker.models import Task


class CreateTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = [
            'uuid', 'agent_point_date',
            'materials', 'last_card_given', 'num_given_cards',
            'approved_requests', 'employee', 'priority'
        ]

        def create(self, validated_data):
            task = Task(
                agent_point_date=validated_data['agent_point_date'],
                materials=validated_data['materials'],
                last_card_given=validated_data['last_card_given'],
                num_given_cards=validated_data['num_given_cards'],
                adress=validated_data['address']
            )
            task.save()


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'address', 'work_time', 'priority',
            'status', 'appointment_date', 'task_type'
        ]
