from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    short_name = serializers.SerializerMethodField()

    def get_short_name(self, obj):
        initials = '.'.join([name[0] for name in [obj.first_name, obj.middle_name] if name]) + "."
        return f"{obj.last_name} {initials}"

    class Meta:
        model = User
        fields = [
                  'last_name', 'first_name', 'role', 'middle_name', 'short_name'
        ]

