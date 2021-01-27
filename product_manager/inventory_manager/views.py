from django.shortcuts import render
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Product
from django.contrib.auth.mixins import LoginRequiredMixin



def home(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'inventory_manager/home.html', context)

class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'inventory_manager/home.html'
    context_object_name = 'products'
    ordering = ['name']
    paginate_by = 5

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['name','code','location','price','quantity']

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ['name','code','location','price','quantity']

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = '/'

class SearchView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'inventory_manager/search.html'
    context_object_name = 'search_results'
    ordering = ['name']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search')
        return context

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult_1 = Product.objects.filter(code__contains=query)
            postresult_2 = Product.objects.filter(name__contains=query)
            if postresult_1:
                result = postresult_1
            else:
                result = postresult_2
        else:
            result = None
        return result
            