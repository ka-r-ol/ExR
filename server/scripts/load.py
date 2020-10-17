
from rest.models import Expense, Category
from django.contrib.auth.models import User
import csv
import datetime
from django.utils import timezone
import random


FILE_NAME = 'scripts/expenses.csv'
USERS = ['Adam', 'Eve']
CATEGORIES = [
    'Clothing',
    'Debt',
    'Education',
    'Entertainment',
    'Food',
    'Gifts/Donations',
    'Household Supplies',
    'Housing',
    'Insurance',
    'Medical and Healthcare',
    'Personal',
    'Retirement',
    'Savings',
    'Transportation',
    'Utilities']


def run():
    Expense.objects.all().delete()
    Category.objects.all().delete()

    current_tz = timezone.get_current_timezone()

    # with open(FILE_NAME, newline='') as csvfile:
    # expenses = csv.reader(csvfile, delimiter=';')
    # headers = next(expenses, None)
    xyz = 1
    for i in range(1000):
        # category;owner;cost;date;name
        category = random.choice(CATEGORIES)
        username = random.choice(USERS)
        cost = random.randint(1, 1000)

        date = datetime.date.today()+datetime.timedelta(days=-random.randint(0, 120))
        name = f"{username}'s purchase of {category} {xyz:>5}"
        xyz += 1
        passw = f"Pass4{username}!"

        u, created = User.objects.get_or_create(username=username)
        if created:
            u.set_password(passw)
            u.is_staff = True
            u.save()

        c, created = Category.objects.get_or_create(name=category)
        if created:
            c.save()

        e, created = Expense.objects.get_or_create(
            name=name, cost=cost, date=date, category=c, owner=u)
        if created:
            e.save()
        print(".", end="")
    print(f"\nData imported. Done!")
