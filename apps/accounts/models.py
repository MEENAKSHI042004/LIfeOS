from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    productivity_score = models.FloatField(default=0.0)

    focus_mode = models.BooleanField(default=False)

    daily_budget_limit = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    def __str__(self) -> str:
        return self.username
class Profile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    timezone = models.CharField(
        max_length=100,
        default='UTC'
    )

    preferred_currency = models.CharField(
        max_length=10,
        default='USD'
    )

    focus_hours_start = models.TimeField(
        null=True,
        blank=True
    )

    focus_hours_end = models.TimeField(
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return f"{self.user.username} Profile"
class UserActivity(models.Model):

    EVENT_CHOICES = [
        ('habit_completed', 'Habit Completed'),
        ('transaction_added', 'Transaction Added'),
        ('goal_updated', 'Goal Updated'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    event_type = models.CharField(
        max_length=100,
        choices=EVENT_CHOICES
    )

    metadata = models.JSONField(default=dict)

    timestamp = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['-timestamp']

    def __str__(self) -> str:
        return f"{self.user.username} - {self.event_type}"
    
