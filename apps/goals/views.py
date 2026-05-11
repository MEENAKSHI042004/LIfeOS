from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Goal
from services.activity_logger import log_event


@api_view(['POST'])
def update_goal(request):
    """
    Update goal progress + log event
    """

    goal_id = request.data.get("goal_id")
    progress = request.data.get("progress")

    goal = Goal.objects.get(id=goal_id, user=request.user)

    goal.progress = progress

    # check completion
    if goal.progress >= 100:
        goal.status = "completed"
    goal.save()

    # 🔥 EVENT LOGGING
    log_event(
        user=request.user,
        event_type="goal_updated",
        metadata={
            "goal_title": goal.title,
            "progress": goal.progress,
            "status": goal.status
        }
    )

    return Response({
        "message": "Goal updated",
        "progress": goal.progress
    })