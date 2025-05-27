from rest_framework import serializers
from .models import Habit

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ['id', 'title', 'days_of_week', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at'] 