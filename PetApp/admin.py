from django.contrib import admin
from .models import *


admin.site.register(SiteUser)
admin.site.register(Seller)
admin.site.register(Category)
admin.site.register(Goods)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(GoodsOrder)
admin.site.register(GoodsCategory)
