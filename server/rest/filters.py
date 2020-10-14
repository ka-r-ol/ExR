from django_filters import rest_framework as filters

from rest.models import Expense, Category
from django.contrib.auth.models import User


class ExpenseFilter(filters.FilterSet):
    # cost_min=, cost_max=
    cost = filters.RangeFilter(field_name="cost")
    # date_before=, date_after=
    date = filters.DateFromToRangeFilter(field_name="date")
    # name =
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    # category__name =
    category__name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Expense
        fields = ['name',  'date', 'cost', 'category']
