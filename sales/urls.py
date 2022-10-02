from django.urls import path
from . import views

app_name = "sales"

urlpatterns = [
    path("", views.add_sales_transaction, name="add_sales_transaction")
]
