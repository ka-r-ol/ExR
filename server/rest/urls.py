from django.urls import include, path
from rest_framework import routers
from rest import views


urlpatterns = [
    path('expenses', views.ExpenseListCreateView.as_view()),
    path('categories', views.CategoryListCreateView.as_view()),
    path('me', views.Me.as_view()),
    path('expense/new', views.ExpenseListCreateView.as_view()),
    path('category/new', views.CategoryListCreateView.as_view()),
    path('expense/<int:pk>', views.ExpenseRetriveUpdateDestroyView.as_view()),
    path('category/<int:pk>', views.CategoryRetriveUpdateDestroyView.as_view()),
]
