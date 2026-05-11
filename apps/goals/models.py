from django.conf import settings
from django.db import models
from django.core.exceptions import ValidationError


class Goal(models.Model):

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('completed', 'Completed'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="goals"
    )

    title = models.CharField(max_length=255)

    description = models.TextField(blank=True)

    deadline = models.DateField()

    progress = models.FloatField(default=0)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active'
    )

    # 🚀 AI / analytics ready fields
    priority = models.IntegerField(default=1)  # 1 = low, 5 = high
    category = models.CharField(max_length=100, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        """Validate data before saving"""
        if self.progress < 0 or self.progress > 100:
            raise ValidationError("Progress must be between 0 and 100.")

    def update_status(self):
        """Auto-update goal status based on progress"""
        if self.progress >= 100:
            self.status = 'completed'
        else:
            self.status = 'active'

    def save(self, *args, **kwargs):
        # ensure validation runs
        self.clean()

        # auto status sync
        self.update_status()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Meta:
        ordering = ['-id']   # ✅ ONLY valid attribute


class Milestone(models.Model):
    goal = models.ForeignKey(
        "Goal",
        on_delete=models.CASCADE,
        related_name="milestones"
    )

    title = models.CharField(max_length=255)

    is_completed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title