from django.urls import path
from .views import HabitListCreateView, HabitCompleteView

urlpatterns = [
    path('', HabitListCreateView.as_view(), name='habit-list'),
    path('complete/', HabitCompleteView, name='habit-complete'),
]