from django.urls import path
from .views import (
    dashboard,          # HTML page
    dashboard_view,     # JSON API
    productivity_score,
    live_activity,
    DailyBriefingView,
    ActivityFeedView,
)

urlpatterns = [
    path('dashboard/',      dashboard_view),          # ← API (use in Thunder Client)
    path('dashboard/page/', dashboard),               # ← HTML page (browser only)
    path('score/',          productivity_score),
    path('live/',           live_activity),
    path('briefing/',       DailyBriefingView.as_view(), name='daily-briefing'),
    path('feed/',           ActivityFeedView.as_view(),  name='activity-feed'),
]