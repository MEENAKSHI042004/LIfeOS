from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.goals.models import Goal


@receiver(post_save, sender=Goal)
def goal_saved(sender, instance, created, **kwargs):
    if created:
        print(f"New goal created: {instance.title}")