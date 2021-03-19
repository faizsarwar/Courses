from django.db import models
from django.contrib.auth.models import User
# Create your models here...

class customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class product(models.Model):
    name=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=7,decimal_places=2)
    digital=models.BooleanField(default=False,null=True )
    image=models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url

class order(models.Model):
    customer=models.ForeignKey(customer,on_delete=models.SET_NULL,null=True,blank=True)
    date_ordered=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False)
    transaction_id=models.CharField(max_length=200, default=True,null=True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping=False
        orderitems=self.orderitems_set.all()
        for i in orderitems:
            if i.product.digital==False:
                shipping=True
        return shipping

    @property
    def get_cart_total(self):
        orderitems=self.orderitems_set.all()
        total=sum([item.get_total for item in orderitems ])   #item pe get_total ka method isliye lagaya kiunkay aik say zayada quantity bhi husktii hai
        return total

    @property
    def get_cart_items(self):
        orderitems=self.orderitems_set.all()
        total=sum([item.quantity for item in orderitems ])   #item pe get_total ka method isliye lagaya kiunkay aik say zayada quantity bhi husktii hai
        return total

class orderitems(models.Model):
    product=models.ForeignKey(product,on_delete=models.SET_NULL,null=True)
    order=models.ForeignKey(order,on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=0,null=True,blank=True)
    date_added=models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total=self.product.price*self.quantity
        return total

class shippingaddress(models.Model):
    customer=models.ForeignKey(customer,on_delete=models.SET_NULL,null=True,blank=True)
    order=models.ForeignKey(order,on_delete=models.SET_NULL,null=True,blank=True)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    zip_code=models.CharField(max_length=200)
    state=models.CharField(max_length=200)