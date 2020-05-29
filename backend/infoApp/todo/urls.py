from django.urls import path
from .views import *
from todo import views

urlpatterns = [
	path('', views.ListTodo.as_view()),
	path('<int:pk>/', views.DetailTodo.as_view()),
]