from django.urls import path
from .views import update_goal

urlpatterns = [
    path('update/', update_goal, name='update-goal'),
]