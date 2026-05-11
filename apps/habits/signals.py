from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.habits.models import Habit


@receiver(post_save, sender=Habit)
def habit_saved(sender, instance, created, **kwargs):
    if created:
        print("Habit created")