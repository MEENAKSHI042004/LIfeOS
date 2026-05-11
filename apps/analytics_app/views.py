"""
Analytics App Views - Fixed Version
"""
from __future__ import annotations

from datetime import date, timedelta
from typing import Any

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.accounts.models import User
from apps.analytics_app.models import UserActivity

from services.productivity_engine import calculate_overall_score
from services.activity_feed_service import get_user_activity_feed
from services.recommendation_engine import generate_daily_recommendation


# ── 1. HTML DASHBOARD (browser only, NOT for Thunder Client) ──────────────
@login_required
def dashboard(request) -> Any:
    """Renders the HTML dashboard page. Not a JSON API endpoint."""
    user: User = request.user
    scores = calculate_overall_score(user)
    recent_events = UserActivity.objects.filter(user=user).order_by("-timestamp")[:10]
    ai_briefing = generate_daily_recommendation(user)
    return render(request, "analytics/dashboard.html", {
        "scores": scores,
        "recent_events": recent_events,
        "ai_briefing": ai_briefing,
    })


# ── 2. API: DASHBOARD DATA (use THIS in Thunder Client) ───────────────────
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard_view(request):
    user = request.user
    scores = calculate_overall_score(user)
    activities = UserActivity.objects.filter(user=user).order_by("-timestamp")[:10]
    return Response({
        "scores": scores,
        "activities": [
            {
                "event_type": a.event_type,
                "timestamp": str(a.timestamp),
                "metadata": a.metadata,
            }
            for a in activities
        ]
    })


# ── 3. API: PRODUCTIVITY SCORE ────────────────────────────────────────────
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def productivity_score(request):
    scores = calculate_overall_score(request.user)
    return Response(scores)


# ── 4. API: LIVE ACTIVITY (FIXED — was duplicated & had wrong timedelta) ──
@api_view(['GET'])
@permission_classes([IsAuthenticated])          # ← was missing in your 2nd copy
def live_activity(request):
    now = timezone.now()
    latest = UserActivity.objects.filter(
        user=request.user,                       # ← was missing in your 2nd copy
        timestamp__gte=now - timedelta(minutes=5)  # ← fixed: timedelta not timezone.timedelta
    ).order_by('-timestamp')
    return Response({
        "results": [
            {"event": a.event_type, "time": a.timestamp, "meta": a.metadata}
            for a in latest
        ]
    })


# ── 5. API: DAILY BRIEFING ────────────────────────────────────────────────
class DailyBriefingView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "ai_insight": generate_daily_recommendation(request.user),
            "recent_activity": get_user_activity_feed(request.user, limit=5),
        })


# ── 6. API: ACTIVITY FEED ─────────────────────────────────────────────────
class ActivityFeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        feed = get_user_activity_feed(user=request.user, limit=20)
        return Response({"count": len(feed), "results": feed})