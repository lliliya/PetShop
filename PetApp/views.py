from django.views.generic import ListView, DetailView
from .models import Seller, Product, Category, Order, Review


class IndexList(ListView):
    template_name = 'index.html'


class SellersList(ListView):
    model = Seller
    ordering = 'name'
    template_name = 'sellers.html'
    context_object_name = 'sellers'


class ProductsList(ListView):
    model = Product
    ordering = 'name'
    template_name = 'products.html'
    context_object_name = 'products'


class CategoryList(ListView):
    model = Category
    ordering = 'name'
    template_name = 'category.html'
    context_object_name = 'category'


class OrderList(ListView):
    model = Order
    ordering = 'time_in'
    template_name = 'orders.html'
    context_object_name = 'orders'


class ReviewsList(ListView):
    model = Review
    ordering = 'user'
    template_name = 'reviews.html'
    context_object_name = 'reviews'


class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'


class SellerDetail(DetailView):
    model = Seller
    template_name = 'seller.html'
    context_object_name = 'seller'


class ReviewDetail(DetailView):
    model = Review
    template_name = 'review.html'
    context_object_name = 'review'
