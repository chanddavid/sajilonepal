
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATE_CHOICES = (
    ('Provience_1', 'Provience_1'),
    ('Provience_2', 'Provience_2'),
    ('Provience_3', 'Provience_3'),
    ('Provience_4', 'Provience_4'),
    ('Provience_5', 'Provience_5'),
    ('Gandaki', 'Gandaki'),
    ('Sudurpaschim', 'Sudurpaschim'),

)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    provience = models.CharField(choices=STATE_CHOICES, max_length=100)
    post_code = models.IntegerField()

    def __str__(self):
        return str(self.id)


PRODUCT_CHOICES = (
    ('M', 'mobile'),
    ('C', 'camera'),
    ('T', 'tshirt'),
    ('HP', 'headphone'),
)


class Product(models.Model):
    title = models.CharField(max_length=50)
    seling_price = models.FloatField()
    discount_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=20)
    category = models.CharField(choices=PRODUCT_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def total_cost_per_item(self):
        return self.quantity * self.product.seling_price


STATUS = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On the Way', 'On the Way'),
    ('Delivered', 'Delivered'),
    ('Cancle', 'Cancle'),
)


class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(choices=STATUS, max_length=50, default='pending')

    def __str__(self):
        return str(self.id)

    @property
    def total_cost_per_item(self):
        return self.quantity * self.product.seling_price
