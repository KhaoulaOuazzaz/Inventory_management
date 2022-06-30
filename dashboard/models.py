from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORY = (
    ('Stationary', 'Stationary'),
    ('Electronics', 'Electronics'),
    ('Food', 'Food'),
)

STATES= (
    ('treated','treated'),
    ('not treated yet','not treated yet')
)

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    quantity = models.PositiveIntegerField(null=True)
    price = models.PositiveIntegerField(null=True)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True)
   

    def __str__(self):
        return f'{self.name}-{self.quantity}'

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, models.CASCADE,null=True)
    order_quantity=models.PositiveBigIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    state= models.CharField(max_length=50, choices=STATES, null=True)


    def __str__(self):
        return f'{self.product} ordered by {self.staff.username}'


class Provider(models.Model):
    p_name = models.CharField(max_length=100, null=True)
    p_mail = models.EmailField(max_length=254)
    p_phone = models.CharField(max_length=100, null=True)
    p_web = models.CharField(max_length=100, null=True)
    p_ados = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.p_name}-{self.p_ados}-{self.p_phone}-{self.p_web}-{self.p_mail}'
              

