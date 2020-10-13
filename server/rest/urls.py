from django.urls import include, path
from rest_framework import routers
from rest import views


urlpatterns = [
    path('expenses', views.ExpenseList.as_view()),
    path('categories', views.CategoryList.as_view()),
    path('users', views.UserList.as_view()),
    #    path('expense/new', views.ExpenseNew.as_view()),
    #    path('category/new', views.CategoryNew.as_view()),
    #    path('expense/<int:id>', views.Expense.as_view()),
    #    path('category/<int:id>', views.Category.as_view()),
]
