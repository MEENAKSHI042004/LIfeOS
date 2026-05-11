from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Habit, HabitLog
from .serializers import HabitSerializer
from services.activity_logger import log_event


class HabitListCreateView(generics.ListCreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def HabitCompleteView(request):
    habit_id = request.data.get("habit_id")
    habit = Habit.objects.get(id=habit_id, user=request.user)
    HabitLog.objects.create(habit=habit)
    habit.streak_count += 1
    habit.save()
    log_event(
        user=request.user,
        event_type="habit_completed",
        metadata={
            "habit_name": habit.title,
            "streak": habit.streak_count,
        }
    )
    return Response({
        "message": "Habit completed",
        "streak": habit.streak_count
    })