from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Sale, Item, Category
from .forms import SaleForm



class SaleCreateView(CreateView):
    model = Sale
    form_class = SaleForm
    template_name = "sales/add.html"
    success_url = reverse_lazy('add')

def load_items(request):
    category_id = request.GET.get('category')
    items = Item.objects.filter(category_id=category_id).order_by('item')
    print(items)
    return render(request, 'sales/item_options.html', context={'items': items})

# class PersonListView(ListView):
#     model = Person
#     context_object_name = 'people'

# class PersonUpdateView(UpdateView):
#     model = Person
#     fields = ('name', 'birthdate', 'country', 'city')
#     success_url = reverse_lazy('person_changelist')
