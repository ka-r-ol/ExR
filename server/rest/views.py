from rest.models import Expense, Category
from django.contrib.auth.models import User

#from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView
#from rest_framework.exceptions import ValidationError
from rest_framework import permissions
from rest.serializers import CategorySerializer, ExpenseSerializer, UserSerializer


class ExpenseList(ListAPIView):
    queryset = Expense.objects.all().order_by('name')
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryList(ListAPIView):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class UserList(ListAPIView):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
