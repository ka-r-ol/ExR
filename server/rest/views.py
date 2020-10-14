from rest.models import Expense, Category
from django.contrib.auth.models import User

#from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
#from rest_framework.exceptions import ValidationError
from rest_framework import permissions
from django_filters import rest_framework as filters
from rest.serializers import CategorySerializer, ExpenseSerializer, UserSerializer
from rest.filters import ExpenseFilter


class ExpenseList(ListAPIView):
    #queryset = Expense.objects.all().order_by('id')
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ExpenseFilter

    def get_queryset(self, *args, **kwargs):
        return Expense.objects.all().filter(owner=self.request.user).order_by('-date', '-created')


class CategoryList(ListAPIView):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class Me(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, queryset=None):
        return User.objects.get(id=self.request.user.id)
