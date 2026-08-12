from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Product

class TopView(TemplateView):
    template_name = 'top.html'

class ProductListView(ListView):
    model = Product
    template_name = 'crud/product_list.html'
    
class ProductDetailView(DetailView):
    model = Product
    template_name = 'crud/product_detail.html'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'crud/product_form.html'
    fields = ['name', 'price', 'description']
    success_url = reverse_lazy('list')


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'crud/product_form.html'
    fields = ['name', 'price', 'description']
    success_url = reverse_lazy('list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'crud/product_confirm_detail.html'
    success_url = reverse_lazy('list')
