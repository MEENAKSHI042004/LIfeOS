from rest_framework import serializers
from .models import Habit, HabitLog


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = [
            'id',
            'title',
            'frequency',
            'streak_count',
            'created_at'
        ]
        read_only_fields = ['streak_count', 'created_at']


class HabitLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = HabitLog
        fields = [
            'id',
            'habit',
            'completed_at'
        ]
        read_only_fields = ['completed_at']