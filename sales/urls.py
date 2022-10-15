from django.urls import path
from . import views

app_name = "sales"

urlpatterns = [
    path("", views.SaleCreateView.as_view(), name="add"),
    path("transactions/", views.SaleTransactions.as_view(), name="transactions"),

    path('ajax/load-items/', views.load_items, name='ajax_load_items'),
]
