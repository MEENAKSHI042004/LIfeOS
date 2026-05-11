from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth import get_user_model

User = get_user_model()


@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if created:
        print(f"New user created: {instance.username}")
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.analytics.models import Insight


@receiver(post_save, sender=Insight)
def insight_created(sender, instance, created, **kwargs):
    if created:
        print("AI Insight generated")