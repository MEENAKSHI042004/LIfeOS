from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Transaction
from services.activity_logger import log_event


@api_view(['POST'])
def create_transaction(request):
    """
    Create a financial transaction + log event
    """

    data = request.data

    transaction = Transaction.objects.create(
        user=request.user,
        amount=data.get("amount"),
        category_id=data.get("category_id"),
        note=data.get("note", "")
    )

    # 🔥 EVENT LOGGING (IMPORTANT)
    log_event(
        user=request.user,
        event_type="transaction_created",
        metadata={
            "amount": str(transaction.amount),
            "category": transaction.category.name
        }
    )

    return Response({
        "message": "Transaction created",
        "id": transaction.id
    })
