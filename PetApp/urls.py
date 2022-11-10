from django.urls import path
from .views import ProductsList, ProductDetail, SellersList, ReviewsList, SellerDetail, ReviewDetail


urlpatterns = [
    path('', ProductsList.as_view()),
    path('<int:pk>', ProductDetail.as_view()),
    path('', SellersList.as_view()),
    path('<int:pk>', SellerDetail.as_view()),
    path('', ReviewsList.as_view()),
    path('<int:pk>', ReviewDetail.as_view()),
]
