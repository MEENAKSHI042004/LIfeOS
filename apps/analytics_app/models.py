from django.db import models
from django.conf import settings


class UserActivity(models.Model):

    EVENT_TYPES = [
        ('habit_completed', 'Habit Completed'),
        ('transaction_created', 'Transaction Created'),
        ('goal_updated', 'Goal Updated'),
        ('ai_warning', 'AI Warning'),
        ('productivity_update', 'Productivity Update'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='activities'
    )

    event_type = models.CharField(
        max_length=50,
        choices=EVENT_TYPES
    )

    metadata = models.JSONField(default=dict)

    timestamp = models.DateTimeField(
        auto_now_add=True
    )

class Meta:
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['timestamp']),
            models.Index(fields=['event_type']),
        ]

def __str__(self):
        return f"{self.user.email} - {self.event_type}"
class EventType(models.TextChoices):
    HABIT_COMPLETED = "habit_completed"
    TRANSACTION_CREATED = "transaction_created"
    GOAL_UPDATED = "goal_updated"
    GOAL_COMPLETED = "goal_completed"