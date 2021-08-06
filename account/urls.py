from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('form/', views.account_view, name="form"),
    path('delete/<str:pk>/', views.delete, name="delete")
]
