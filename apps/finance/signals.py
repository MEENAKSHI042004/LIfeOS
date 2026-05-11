from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Transaction
from services.activity_logger import log_event as log_user_activity


@receiver(post_save, sender=Transaction)
def log_transaction_activity(
    sender,
    instance,
    created,
    **kwargs
):

    if created:

        log_user_activity(
            user=instance.user,
            event_type='transaction_added',
            metadata={
                'amount': float(instance.amount),
                'category': instance.category.name,
            }
        )
@receiver(post_save, sender=Transaction)
def transaction_saved(sender, instance, created, **kwargs):
    if created:
        print(f"New transaction added: {instance.amount}")