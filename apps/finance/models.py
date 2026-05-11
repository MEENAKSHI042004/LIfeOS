from django.conf import settings
from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Transaction(models.Model):

    TRANSACTION_TYPES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    transaction_type = models.CharField(
        max_length=20,
        choices=TRANSACTION_TYPES
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    note = models.TextField(blank=True)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self) -> str:
        return f"{self.user.username} - {self.amount}"


class Budget(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    monthly_limit = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    month = models.DateField()

    def __str__(self) -> str:
        return f"{self.user.username} Budget"