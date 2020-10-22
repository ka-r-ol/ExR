
from rest.models import Expense, Category
from django.contrib.auth.models import User
import csv
import datetime
from django.utils import timezone
import random


FILE_NAME = 'scripts/expenses.csv'
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


class Generator:
    def __init__(self, n_total):
        Expense.objects.all().delete()
        Category.objects.all().delete()
        self.counter = 1
        self.n_total = n_total

    def __call__(self, username, number):
        for i in range(number):
            self.add_record(username)

    def add_record(self, username):
        category = random.choice(CATEGORIES)
        # username = random.choice(USERS)
        cost = random.randint(1, 1000)

        date = datetime.date.today()+datetime.timedelta(days=-random.randint(0, 120))
        name = f"{username}'s purchase of {category} {self.counter:>5}"
        self.counter += 1
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
        if self.counter % 100 == 0:
            print(f"{self.counter:>11,} / {self.n_total:,}".replace(",", " "))


def run():

    start_time = datetime.datetime.now().replace(microsecond=0)
    n_Eve = 20
    n_Adam = 10*365*2

    generator = Generator(n_Eve+n_Adam)

    generator("Eve", n_Eve)
    generator("Adam", n_Adam)

    end_time = datetime.datetime.now().replace(microsecond=0)
    print(
        f"\nData imported. Done! {n_Eve+n_Adam} records in {end_time-start_time}")
