import uuid
from django.db import models
from django.contrib.auth.models import User
from apps.products.models import Product

class Order(models.Model):
    
    pub_id=models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    
    user= models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders',
    )
    
    accepting_time = models.DateTimeField('Accepting time')
    
    completing_or_rejecting_time = models.DateTimeField('Completing or rejecting time', blank=True, null=True)
    
    status_choices=[
        ('accepted','accepted'),
        ('completed','completed'),
        ('rejected','rejected'),
        ('cancelled','cancelled')
    ]
    status=models.CharField(
        max_length = 20,
        choices=status_choices,
        default='accepted'
    )
    
    is_paid=models.BooleanField(default=False)
    
    comment= models.TextField(max_length=500, blank=True)
    
    @property
    def is_editable(self):
        if self.status=='accepted' and self.is_paid==False:
            return True
        else:
            return False
            
    @property
    def max_orderitems(self):
        if len(self.orderitems.all())<5:
            return False
        else:
            return True
    
    def __str__(self):
        return 'Order#{}  ({}) for {}'.format(self.id, self.pub_id, self.user)
        
        
class OrderItem(models.Model):

    pub_id=models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    
    order = models.ForeignKey(
        Order, 
        on_delete=models.CASCADE, 
        related_name='orderitems'
    )
    
    product=models.ForeignKey(
        Product, 
        on_delete=models.CASCADE
    )
    
    amount = models.IntegerField(default=1)
    
    def __str__(self):
        return '{}: {}  - {} items'.format(self.order, self.product, self.amount)
        
