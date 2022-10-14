from django.db import models
from django.contrib.auth.models import User


class SiteUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Seller(models.Model):
    name = models.CharField(max_length=50, unique=True, default='NoName')
    seller_rating = models.FloatField(default=0.0)
    contacts = models.TextField(default='The seller did not specify his contacts')

    def update_rating(self):
        self.seller_rating = 0
        for order in Order.objects.filter(seller_id=self.name):
            self.seller_rating += order.order_rating
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, default='NoName')


class Goods(models.Model):
    vendor_code = models.IntegerField(default=0)
    name = models.CharField(max_length=50, default='NoName')
    price = models.FloatField(default=0.00)
    weight = models.FloatField(default=0.00)
    description = models.TextField(default='Description not specified')
    composition = models.TextField(default='Сomposition not specified')
    category = models.ManyToManyField(Category, through='GoodsCategory')
    product_rating = models.IntegerField(default=0)

    def like(self, amount=0):
        self.product_rating += amount
        self.save()

    def dislike(self):
        self.like(-1)


class Order(models.Model):
    client = models.ManyToManyField(SiteUser, through='OrderSiteUser')
    time_in = models.DateTimeField(auto_now_add=True)
    time_out = models.DateTimeField(null=True)
    cost = models.FloatField(default=0.00)
    pickup = models.BooleanField(default=False)  # if pickup, then True, if delivery, then False
    complete = models.BooleanField(default=False)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    goods = models.ManyToManyField(Goods, through='GoodsOrder')
    order_rating = models.IntegerField(default=0)

    def like(self, amount=0):
        self.order_rating += amount
        self.save()

    def dislike(self):
        self.like(-1)


class Review(models.Model):
    datetime_creation = models.DateTimeField(auto_now_add=True)
    product = models.ManyToManyField(Goods, through='GoodsReview')
    user = models.ManyToManyField(SiteUser, through='SiteUserReview')
    order = models.ManyToManyField(Order, through='OrderReview')
    text = models.TextField(default='No Text')


class GoodsOrder(models.Model):
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)


class GoodsCategory(models.Model):
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class GoodsReview(models.Model):
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)


class SiteUserReview(models.Model):
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)


class OrderReview(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)


class OrderSiteUser(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    client = models.ForeignKey(SiteUser, on_delete=models.CASCADE)
