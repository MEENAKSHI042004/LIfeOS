from typing import Any

from apps.finance.models import Transaction
from apps.habits.models import HabitLog
from apps.goals.models import Goal


# ==========================================
# PRODUCTIVITY SCORE
# ==========================================

def calculate_productivity_score(user: Any) -> float:

    completed_habits = HabitLog.objects.filter(
        habit__user=user
    ).count()

    completed_goals = Goal.objects.filter(
        user=user,
        status='completed'
    ).count()

    score = (
        completed_habits * 5
    ) + (
        completed_goals * 20
    )

    return round(min(score, 100), 2)


# ==========================================
# HABIT CONSISTENCY
# ==========================================

def calculate_habit_consistency(user: Any) -> float:

    total_habits = user.habits.count()

    completed_logs = HabitLog.objects.filter(
        habit__user=user
    ).count()

    if total_habits == 0:
        return 0.0

    score = (
        completed_logs / (total_habits * 10)
    ) * 100

    return round(min(score, 100), 2)


# ==========================================
# FINANCIAL HEALTH
# ==========================================

def calculate_financial_health(user: Any) -> float:

    total_spent = Transaction.objects.filter(
        user=user,
        transaction_type='expense'
    ).count()

    budget_limit = float(
        user.daily_budget_limit or 5000
    )

    if budget_limit == 0:
        return 0.0

    score = 100 - (
        (total_spent / budget_limit) * 100
    )

    return round(max(score, 0), 2)


# ==========================================
# GOAL COMPLETION RATE
# ==========================================

def calculate_goal_completion(user: Any) -> float:

    total_goals = Goal.objects.filter(
        user=user
    ).count()

    completed_goals = Goal.objects.filter(
        user=user,
        status='completed'
    ).count()

    if total_goals == 0:
        return 0.0

    score = (
        completed_goals / total_goals
    ) * 100

    return round(score, 2)


# ==========================================
# GOAL FAILURE PREDICTION
# ==========================================

def predict_goal_failure(user: Any) -> float:

    incomplete_goals = Goal.objects.filter(
        user=user,
        status='active'
    ).count()

    missed_habits = max(
        0,
        user.habits.count() -
        HabitLog.objects.filter(
            habit__user=user
        ).count()
    )

    risk_score = (
        incomplete_goals * 10
    ) + (
        missed_habits * 5
    )

    return round(min(risk_score, 100), 2)


# ==========================================
# SPENDING ANOMALY DETECTION
# ==========================================

def detect_spending_anomaly(user: Any) -> bool:

    recent_expenses = Transaction.objects.filter(
        user=user,
        transaction_type='expense'
    ).count()

    return recent_expenses > 10


# ==========================================
# DAILY AI RECOMMENDATION
# ==========================================

def generate_daily_briefing(user: Any) -> str:

    financial_health = calculate_financial_health(
        user
    )

    habit_score = calculate_habit_consistency(
        user
    )

    productivity = calculate_productivity_score(
        user
    )

    if financial_health < 50:

        return (
            "You are spending aggressively this week. "
            "Reduce food delivery and focus on essentials."
        )

    if habit_score < 50:

        return (
            "Your habit consistency is dropping. "
            "Focus on completing your morning routine today."
        )

    if productivity > 70:

        return (
            "Excellent productivity momentum. "
            "Keep maintaining your study and workout streaks."
        )

    return (
        "You overspent yesterday and missed 2 habits. "
        "Focus on completing your habits and reducing "
        "unnecessary spending today."
    )