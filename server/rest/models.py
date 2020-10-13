from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.conf import settings


class Category(models.Model):
    name = models.TextField(
        max_length=100,
        validators=[MinLengthValidator(
            2, "Category name must be greater than 2 characters")],
        unique=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if len(self.name) < 15:
            return self.name
        return self.name[:11] + ' ...'


class Expense(models.Model):
    name = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(
            3, "Expense name must be greater than 3 characters")]
    )
    cost = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    date = models.DateField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ":" + str(self.cost) + " PLN"
