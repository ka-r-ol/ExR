
from rest.models import Expense, Category
from django.contrib.auth.models import User
import csv
from datetime import datetime
from django.utils import timezone


FILE_NAME = 'scripts/expenses.csv'


def run():
    Expense.objects.all().delete()
    Category.objects.all().delete()

    current_tz = timezone.get_current_timezone()

    with open(FILE_NAME, newline='') as csvfile:
        expenses = csv.reader(csvfile, delimiter=';')
        headers = next(expenses, None)
        for row in expenses:
            # category;owner;cost;date;name
            category = row[0]
            username = row[1]
            cost = float(row[2])
            date = current_tz.localize(
                datetime.strptime(row[3], '%d/%m/%Y'))
            name = row[4]
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
    print(f"\n{FILE_NAME} imported. Done!")
