from django.views.generic import ListView
from .models import Seller, Goods, Category, Order, Review


class IndexList(ListView):
    template_name = 'index.html'


class SellerList(ListView):
    model = Seller
    ordering = 'name'
    template_name = 'sellers.html'
    context_object_name = 'sellers'


class GoodsList(ListView):
    model = Goods
    ordering = 'name'
    template_name = 'flatpages/goods.html'
    context_object_name = 'goods'


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


class ReviewList(ListView):
    model = Review
    ordering = 'user'
    template_name = 'reviews.html'
    context_object_name = 'reviews'
