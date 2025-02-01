from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    role = models.CharField(max_length=50, choices=[('customer', 'Customer'), ('admin', 'Admin')])

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups",  # ✅ Fix clash
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",  # ✅ Fix clash
        blank=True
    )

class Card(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=16, unique=True)
    card_type = models.CharField(max_length=10, choices=[('debit', 'Debit'), ('credit', 'Credit')])

class Loan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('approved', 'Approved'), ('pending', 'Pending')])
