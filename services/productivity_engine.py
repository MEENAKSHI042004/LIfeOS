from apps.habits.models import Habit
from apps.finance.models import Transaction
from apps.goals.models import Goal


def calculate_habit_score(user) -> float:
    habits = Habit.objects.filter(user=user)
    if not habits.exists():
        return 0.0
    total_streak = sum(h.streak_count for h in habits)
    return min((total_streak / (habits.count() * 10)) * 100, 100.0)


def calculate_finance_score(user) -> float:
    transactions = Transaction.objects.filter(user=user)
    if not transactions.exists():
        return 100.0
    total_spent = sum(float(t.amount) for t in transactions)
    score = max(100 - (total_spent / 1000), 0)
    return round(score, 2)


def calculate_goal_score(user) -> float:
    goals = Goal.objects.filter(user=user)
    if not goals.exists():
        return 0.0
    avg_progress = sum(float(g.progress) for g in goals) / goals.count()
    return round(avg_progress, 2)


def calculate_overall_score(user) -> dict:
    habit = calculate_habit_score(user)
    finance = calculate_finance_score(user)
    goal = calculate_goal_score(user)
    overall = (habit * 0.4) + (finance * 0.3) + (goal * 0.3)
    return {
        "habit_score": round(habit, 2),
        "finance_score": round(finance, 2),
        "goal_score": round(goal, 2),
        "overall_score": round(overall, 2)
    }


def calculate_productivity_trend(user):
    today_score = calculate_overall_score(user)["overall_score"]
    yesterday_score = calculate_overall_score(user)["overall_score"]
    change = today_score - yesterday_score
    return {
        "current": today_score,
        "trend": round(change, 2),
        "status": "improving" if change > 0 else "declining"
    }