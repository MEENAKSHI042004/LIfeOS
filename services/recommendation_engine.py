from apps.accounts.models import User


def generate_daily_recommendation(user: User) -> str:
    from services.productivity_engine import calculate_overall_score
    scores = calculate_overall_score(user)

    habit = scores["habit_score"]
    finance = scores["finance_score"]
    goal = scores["goal_score"]

    weakest = min(
        [("habit", habit), ("finance", finance), ("goal", goal)],
        key=lambda x: x[1]
    )

    tips = {
        "habit": f"Your habit score is {habit} — focus on completing at least 3 habits before noon today to build momentum.",
        "finance": f"Your finance score is {finance} — review your recent transactions and avoid impulsive spending today.",
        "goal": f"Your goal score is {goal} — spend 30 minutes today making progress on your most important goal.",
    }

    overall = scores["overall_score"]
    if overall >= 80:
        opening = "Great work! You're performing well across all areas."
    elif overall >= 60:
        opening = "You're making solid progress. Keep pushing."
    else:
        opening = "Let's turn things around today — small consistent actions add up."

    return f"{opening} {tips[weakest[0]]}"