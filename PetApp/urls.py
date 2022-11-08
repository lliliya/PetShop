from django.urls import path
from .views import GoodsList


urlpatterns = [
    path('goods/', GoodsList.as_view()),
]
