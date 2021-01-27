from django.urls import path
from . import views
from .views import (
    ProductListView, 
    ProductDetailView, 
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    SearchView
)

urlpatterns = [
    path('', ProductListView.as_view(), name='list-home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='list-detail'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='list-update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='list-delete'),
    path('product/new/', ProductCreateView.as_view(), name='list-create'),
    path('search/', SearchView.as_view(), name='searchbar'),
]