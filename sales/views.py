from django.shortcuts import render

# Create your views here.
def add_sales_transaction(request):
    return render(request, "sales/add_sales_transaction.html")
