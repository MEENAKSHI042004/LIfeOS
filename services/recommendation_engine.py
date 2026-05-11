from typing import Any

from apps.accounts.models import UserActivity
from apps.accounts.models import User
from django.contrib.auth import get_user_model


def log_user_activity(
    user: User,
    event_type: str,
    metadata: dict[str, Any]
) -> None:

    UserActivity.objects.create(
        user=user,
        event_type=event_type,
        metadata=metadata
    )
    from django.contrib.auth import get_user_model

User = get_user_model()


def generate_daily_recommendation(user: User) -> dict:
    """
    Rule-based AI recommendation engine (MVP version)
    """

    return {
        "user_id": user.id,
        "message": "Focus on completing your habits and reduce unnecessary spending today.",
        "insights": [
            "Track your morning routine consistency",
            "Avoid impulsive transactions",
            "Maintain daily streak momentum"
        ],
        "priority": "medium"
    }