#from django.db import models

# Create your models here.

#from django.db import models
#from django.contrib.auth.models import User
from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django import forms




# Create your models here.

class UserManager(BaseUserManager):
     def create_user(self,username, name, email, password=None):
         if not email:
             raise ValueError('User must have an email address')

         user = self.model(
             email=self.normalize_email(email),
             name= name,
             #last_name=last_name,
             #phone=phone, 
         )
         user.set_password(password)
         user.save(using=self._db)
         return user

     def create_superuser(self,name, email, password=None):
        
         user = self.create_user(
              email=self.normalize_email(email),
              password=password,
              name=name,
              #last_name=last_name,
              #phone=phone,
              )
         user.is_admin = True
         user.is_active = True
         user.is_staff = True
         user.is_superadmin = True
         user.role=1
         user.save(using=self._db)
         return user

class CustomUser(AbstractUser):
    ADMIN = 1
    CUSTOMER = 2
    DELIVERYTEAM = 3
    SELLER = 4

    USER_TYPES = (
        (ADMIN, 'Admin'),
        (CUSTOMER, 'Customer'),
        (DELIVERYTEAM, 'Deliveryteam'),
        (SELLER,'Seller'),
    )

    #username=None
    user_types = models.PositiveSmallIntegerField(choices=USER_TYPES,default='2')
    
    username=models.CharField(max_length=50,unique=True)
    name = models.CharField(max_length=50)


    #last_name = models.CharField(max_length=50)
    #USERNAME_FIELD = 'email'
    email = models.EmailField(max_length=100, unique=True)
    #phone = models.CharField(max_length=12, blank=True)
    password = models.CharField(max_length=128)
   # confirmPassword = models.CharField(max_length=128)
    #role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, blank=True, null=True,default='1')



    #usertype=SELLER starts

    shop_name=models.CharField(max_length=255, null=True)
    user_name=models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=128)
    phone = models.CharField(max_length=12, blank=True)
    shop_address=models.CharField(max_length=255, null=True)
    tax_id=models.CharField(max_length=20, null=True)
    

    #  #usertype=SELLER ends








    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)

    
    #REQUIRED_FIELDS = ['first_name','last_name', 'phone']

    objects = UserManager()

    def str(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True



class UserProfile(models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='media/profile_picture', blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    addressline1 = models.CharField(max_length=50, blank=True, null=True)
    addressline2 = models.CharField(max_length=50, blank=True, null=True)
    # country = models.CharField(max_length=15, default="India", blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    pin_code = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    profile_created_at = models.DateTimeField(auto_now_add=True)
    profile_modified_at = models.DateTimeField(auto_now=True)


    def calculate_age(self):
        today = date.today()
        age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        return age
    age = property(calculate_age)


    def get_gender_display(self):
        return dict(self.GENDER_CHOICES).get(self.gender)

    def str(self):
        return self.user.email
    
    def get_role(self): 
        if self.user_type == 2:
            
            user_role = 'Customer'
        elif self.user_type == 3:
            user_role = 'Deliveryteam'
        elif self.user_type == 4:
            user_role = 'Seller'
        
        return user_role







class Age(models.Model):
    id = models.AutoField(primary_key=True)
    age_range = models.CharField(max_length=20)

    def __str__(self):
        return self.age_range

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Add the foreign key to Category



    def __str__(self):
        return self.name

class Product(models.Model):
    

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    age = models.ForeignKey(Age, on_delete=models.CASCADE)
    material = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    
    gender = models.CharField(max_length=20)
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('Available', 'Available'), ('Not Available', 'Not Available')])
    product_image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name



class WishlistItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def _str_(self):
        return self.product.name




#add to cart start
class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    products = models.ManyToManyField(Product, through='CartItem')

    def __str__(self):
        return f"Cart for {self.user.username}"



#payment
class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_id = models.CharField(max_length=100, null=True, blank=True)
    payment_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Order {self.id} by {self.user.username}"



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    item_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order {self.order.id}"





#cmd  -- python manage.py makemigrations
#        python manage.py migrate



#python manage.py makemigrations
#python manage.py migrate