from rest.models import Expense, Category
from django.contrib.auth.models import User
#from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
#from rest_framework.exceptions import ValidationError
from rest_framework import permissions
from rest_framework.response import Response
from django_filters import rest_framework as filters
from rest.serializers import CategorySerializer, ExpenseSerializer, UserSerializer
from rest.filters import ExpenseFilter


class ExpenseListCreateView(ListCreateAPIView):
    #queryset = Expense.objects.all().order_by('id')
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ExpenseFilter

    def get_queryset(self, *args, **kwargs):
        return Expense.objects.all().filter(owner=self.request.user).order_by('-date', '-created')


class CategoryListCreateView(ListCreateAPIView):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None


class Me(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, queryset=None):
        return User.objects.get(id=self.request.user.id)


class ExpenseRetriveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ExpenseFilter

    def get_queryset(self, *args, **kwargs):
        return Expense.objects.all().filter(owner=self.request.user).order_by('-date', '-created')


class CategoryRetriveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class Stats(ListAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ExpenseFilter

    def get_queryset(self, *args, **kwargs):
        return Expense.objects.all().filter(owner=self.request.user).order_by('-date', '-created')

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        data = dict()
        for q in queryset:
            if q.category.name in data:
                data[q.category.name]['number'] += 1
                data[q.category.name]['cost'] += q.cost
            else:
                data[q.category.name] = dict()
                data[q.category.name]['number'] = 1
                data[q.category.name]['cost'] = q.cost
        return Response(data)
