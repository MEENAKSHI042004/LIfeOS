from apps.analytics_app.models import UserActivity
from django.contrib.auth import get_user_model

User = get_user_model()


def get_user_activity_feed(user: User, limit: int = 20):
    """
    Returns recent activity feed for dashboard
    """

    activities = (
        UserActivity.objects
        .filter(user=user)
        .order_by('-timestamp')[:limit]
    )

    feed = []

    for activity in activities:
        feed.append({
            "event_type": activity.event_type,
            "metadata": activity.metadata,
            "timestamp": activity.timestamp
        })

    return feed