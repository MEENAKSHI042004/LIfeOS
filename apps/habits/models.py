from django.conf import settings
from django.db import models


class Habit(models.Model):

    FREQUENCY_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='habits'
    )

    title = models.CharField(max_length=255)

    frequency = models.CharField(
        max_length=20,
        choices=FREQUENCY_CHOICES
    )

    streak_count = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class HabitLog(models.Model):

    habit = models.ForeignKey(
        Habit,
        on_delete=models.CASCADE
    )

    completed_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        indexes = [
            models.Index(fields=['completed_at'])
        ]

    def __str__(self):
        return f"{self.habit.title} Log"