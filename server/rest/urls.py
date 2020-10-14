from django.urls import include, path
from rest_framework import routers
from rest import views


urlpatterns = [
    path('expenses', views.ExpenseView.as_view()),
    path('categories', views.CategoryView.as_view()),
    path('me', views.Me.as_view()),
    path('expense/new', views.ExpenseView.as_view()),
    path('category/new', views.CategoryView.as_view()),
    #    path('expense/<int:id>', views.Expense.as_view()),
    #    path('category/<int:id>', views.Category.as_view()),
]
