from django.db import models
from django.contrib.auth.models import User
from datetime import date,datetime
import uuid

class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    para1 = models.CharField(max_length=70, default="")
    heading = models.CharField(max_length=70, default="")
    bg_img = models.ImageField(upload_to='images', default='')

    class Meta:
        abstract = True 

    def __str__(self):
        return str(self.id)
    
class slider1(BaseModel):
    para2 = models.CharField(max_length=70, default="")

class slider2(BaseModel):
  heading = None
  
class banner(BaseModel):
   para1 = None
    
class services(BaseModel):
    pass
    
class Blog(BaseModel):
    fashion = models.CharField(max_length=70, default="")
    para2 = models.CharField(max_length=70, default="")

class instaPic(BaseModel):
    bg_img = models.ImageField(upload_to='images', default='')
    para1 = None
    heading = None

class discount_offer(BaseModel):
    link = models.CharField(max_length=70, default="")
    bg_img = None

# =================================================home end============================================================

class footer(BaseModel):
    bg_img = None
    para2 = models.CharField(max_length=100, default="")
    para3 = models.CharField(max_length=100, default="")
    link = models.CharField(max_length=100, default="")


class BaseModel2(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    heading = models.CharField(max_length=70, default="")
    link1 = models.CharField(max_length=70, default="")
    link2 = models.CharField(max_length=70, default="")
    link3 = models.CharField(max_length=70, default="")
    link4 = models.CharField(max_length=70, default="")

    class Meta:
        abstract = True 

    def __str__(self):
        return str(self.id)

class column1(BaseModel2):
    pass

class column2(BaseModel2):
    pass

class column3(BaseModel2):
    pass

class colunm4(BaseModel2):
    pass

#============================================================ footer end============================================================

class shop_offer(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    heading = models.CharField(max_length=70, default="")
    dropButton = models.CharField(max_length=70,default='')
    dropdown1 = models.CharField(max_length=70,default='')
    dropdown2 = models.CharField(max_length=70,default='')
    dropdown3 = models.CharField(max_length=70,default='')

class filter_product(BaseModel):
    hover_img = models.ImageField(upload_to='images')

# ============================================================shop end ============================================================

class blogList(BaseModel):
    para2 = models.CharField(max_length=70, default="")
    link = models.CharField(max_length=100, default="")

class catogery(BaseModel2):
    pass
    
class Latest_Post(BaseModel):
    pass
    
class Tags(BaseModel2):
    link5 = models.CharField(max_length=70, default="")
    link6 = models.CharField(max_length=70, default="")
    link7 = models.CharField(max_length=70, default="")
    link8 = models.CharField(max_length=70, default="")
    bg_img = models.ImageField(upload_to='images', default='')   

# ============================================================blog end ============================================================


class contact_heading(BaseModel):
    bg_img = None
    heading2 = models.CharField(max_length=100, default="")
    heading3 = models.CharField(max_length=100, default="")

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    heading1 = models.CharField(max_length=100, default="")
    heading2 = models.CharField(max_length=100, default="")
    heading3 = models.CharField(max_length=100, default="")
    para1 = models.CharField(max_length=100, default="")
    para2 = models.CharField(max_length=100, default="")
    para3 = models.CharField(max_length=100, default="")
    para4 = models.CharField(max_length=100, default="")
    para5 = models.CharField(max_length=100, default="")
    link = models.CharField(max_length=100, default="")

class GetIntoTech(BaseModel):
    bg_img =None

class Customer(BaseModel):
    bg_img =  None
    name = models.CharField(max_length=70,default='')
    email = models.EmailField(max_length=70,default='')
    phoneNo = models.IntegerField(default='')
    website = models.CharField(max_length=170,default='')
    content = models.CharField(max_length=1000,default='')

# ============================================================cart folder ============================================================

class cartheading(BaseModel):
    bg_img = None
    para2 = models.CharField(max_length=70,default='')
    para3 = models.CharField(max_length=70,default='')
    para1 = models.FloatField(default='')

class ifEmpty(BaseModel):
    heading = None
    link = models.CharField(max_length=70,default='')

# ============================================================for wishlist ============================================================

class items(BaseModel):     
    heading = None
    para1 = models.FloatField(default='')
    para2 = models.CharField(max_length=70,default='')
    para3 = models.CharField(max_length=70,default='')
    para4 = models.CharField(max_length=70,default='')
    para5 = models.CharField(max_length=70,default='')
    link = models.CharField(max_length=70,default='')

class box(models.Model):       
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    items = models.ForeignKey(items, on_delete=models.CASCADE, default=None)
    quantity = models.PositiveIntegerField(default=1)

class OptionCart(BaseModel):
    heading = None
    para1 = models.FloatField(default='')
    hover_img = models.ImageField(upload_to='images', default='')
    para2 = models.CharField(max_length=70,default='')
    

class warning(models.Model):
    para = models.CharField(max_length=70,default='')

class footercart(models.Model):
    para1 = models.CharField(max_length=70,default='')
    para2 = models.CharField(max_length=70,default='')


# ============================================================wishlist folder ============================================================

class wishlistheading(BaseModel):
    bg_img = None
    para1 = None

class Wishlist(BaseModel):
    heading = None
    para2 = models.CharField(max_length=70,default='')
    para3 = models.CharField(max_length=70,default='')
    para4 = models.CharField(max_length=70,default='')
    para5 = models.CharField(max_length=70,default='')
    link = models.CharField(max_length=70,default='')


class Optionwishlist(BaseModel):
    heading = None
    hover_img = models.ImageField(upload_to='images', default='')
    para2 = models.CharField(max_length=70,default='')
    
class EmptyWishlist(BaseModel):
    heading = None
    link = models.CharField(max_length=70,default='')


# ============================================================search folder ============================================================

class search(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    heading = models.CharField(max_length=70,default='')
    dropdown1 = models.CharField(max_length=70,default='')
    dropdown2 = models.CharField(max_length=70,default='')
    dropdown3 = models.CharField(max_length=70,default='')

class QuickSearch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    para = models.CharField(max_length=70,default='')
    link1 = models.CharField(max_length=70,default='')
    link2 = models.CharField(max_length=70,default='')
    link3 = models.CharField(max_length=70,default='')

class OptionSearch(BaseModel):
    heading = None
    hover_img = models.ImageField(upload_to='images', default='')
    para2 = models.CharField(max_length=70,default='')  

# ============================================================account form ============================================================

class account(models.Model):    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    heading1 = models.CharField(max_length=70,default='') 
    heading2 = models.CharField(max_length=70,default='') 

#============================================================ for home page============================================================

class handPicked_product(BaseModel):       
    hover_img = models.ImageField(upload_to='images', default='')
    para1 = models.FloatField(default='')
    
class wishlists(models.Model):       
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    productes = models.ForeignKey(handPicked_product, on_delete=models.CASCADE, default='')
    quantity = models.PositiveIntegerField(default=1)
    Date = models.DateField(default=date.today)
    
class User_Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    product = models.ForeignKey(handPicked_product, on_delete=models.CASCADE, default=None)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.para1
    
    def __str__(self):
        return str(self.id)
    
    
class CheckoutAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, blank=True)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.EmailField(default='')
    region = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    apartment = models.CharField(max_length=255, blank=True, default='')
    town = models.CharField(max_length=255, default='')
    postcode = models.IntegerField(default='')
    country = models.CharField(max_length=255, blank=True, default='')
    phoneNo = models.IntegerField(default='')
    OrderNote = models.TextField(blank=True, default='')

class order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, blank=True)
    order_no = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    total_amount = models.PositiveIntegerField() 
    payment_method = models.CharField(max_length=150,default='')

class orderItem(models.Model):
    order_no  = models.ForeignKey(order,on_delete=models.CASCADE, default=None)
    product = models.ForeignKey(handPicked_product, on_delete=models.CASCADE ,default=None)
    quantity =  models.PositiveIntegerField()
