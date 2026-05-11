from apps.analytics_app.models import UserActivity


def log_event(user, event_type: str, metadata: dict = None):
    """
    Centralized event logging function
    """

    if metadata is None:
        metadata = {}

    return UserActivity.objects.create(
        user=user,
        event_type=event_type,
        metadata=metadata
    )