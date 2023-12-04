# from django.shortcuts import render

# # Create your views here.
# def index(request):
#     return render(request,'index.html')

# def register(request):
#     return render(request,'register.html')

# def login(request):
#     return render(request,'login.html')


from django.shortcuts import render,redirect
from .models import CustomUser,UserProfile
from django.contrib.auth import authenticate ,login as auth_login,logout
from django.contrib.auth import login
from django.contrib import messages
from .models import *

from django.views.decorators.cache import never_cache

from django.contrib.auth.decorators import login_required
#here
from django.contrib.auth.models import User

from .models import Product, Age, Brand, Category, Subcategory

from .models import Product

from django.core.exceptions import ValidationError

from django.http import HttpResponseRedirect






# from .forms import ProductForm
# from .forms import ProductForm  # Create this form if you want to use Django forms for validation and handling

 # Create this form if you want to use Django forms for validation and handling

# Create your views here.

@never_cache
def index(request):
    return render(request, 'index.html')


def sellerreg(request):
    return render(request, 'sellerreg.html')



def sellerhome(request):
    return render(request, 'sellerhome.html')


@never_cache
@login_required(login_url='login')
def userhome(request):
    #session start
    # if 'username' in request.session:
    # if request.user.is_authenticated:
        #session end
        return render(request, 'userhome.html')
        #session st
    # return redirect(login)
    #session en



# def about(request):
#     return render(request, 'about.html')
@never_cache
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        # phone = request.POST.get('phone', None)
        password = request.POST.get('password', None)
        confirm_password = request.POST.get('confirm_password', None)
        # role = CustomUser.CUSTOMER
        if username and name and email and password:
            if CustomUser.objects.filter(email=email,username=username).exists():
                messages.success(request,("Email is already registered."))
            
            elif password!=confirm_password:
                messages.success(request,("Password's Don't Match, Enter correct Password"))
            else:
                user = CustomUser(username=username,name=name, email=email)
                user.set_password(password)  # Set the password securely
                user.is_active=True
                user.save()


                messages.success(request, "Registered successfully")



                user_profile = UserProfile(user=user)
                user_profile.save()
                # activateEmail(request, user, email)
                return redirect('login')  
            
    return render(request, 'register.html')

# @never_cache
def login(request):
    #session st
    # if 'username' in request.session:
    if request.user.is_authenticated:

        return redirect(userhome)
        #session en
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        # if user is not None:
        #     auth_login(request, user)
        #     return redirect('/userhome')
        # else:
        #    messages.success(request,("Invalid credentials."))
        # print(username)  # Print the email for debugging
        # print(password)  # Print the password for debugging

        if username and password:
            user = authenticate(request, username =username , password=password)
            if user is not None:

                #session start
                # request.session['username'] = username
                # login(request, user)

                #session end
                auth_login(request,user)

                if request.user.user_types==CustomUser.CUSTOMER:
                
                    return redirect('userhome')
                elif request.user.user_types == CustomUser.SELLER:
                     print("user is seller")
                     return redirect('sellerhome')

                elif request.user.user_types == CustomUser.ADMIN:
                    print("user is admin")                   
                    return redirect('http://127.0.0.1:8000/admin/')
                # else:
                #     print("user is normal")
                #     return redirect('')

            else:
                messages.success(request,("Invalid credentials."))
        else:
            messages.success(request,("Please fill out all fields."))
        
    return render(request, 'login.html')


# def userhome(request):
#     return render(request, 'userhome.html')

@never_cache
@login_required(login_url='login')
def logout_view(request):
     #session st
    # if 'username' in request.session:
    # if request.user.is_authenticated:
        # request.session.flush()
        #session en
        logout(request)
    
    # messages.success(request,("Logged out"))
        return  redirect('login')

# def register_pump(request):
#     return render(request, 'registerPump.html')

# def userhome(request):
#     return render(request, 'userhome.html')

# def about(request):
#     return render(request, 'about.html')
# def contact(request):
#     return render(request, 'contact.html')
# def Pump(request):
#     return render(request, 'Pump.html')
# def base(request):
#     return render(request, 'base.html')


#user table code
# def register_user(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')  # Add email field
#         phone = request.POST.get('phone')
#         password = request.POST.get('password')
#         confirm_password = request.POST.get('cpass')
#         my_user = User.objects.create_user(username=username, email=email, password=password)
#         my_user.save()
#         return redirect('/login')
           
#     #     # Process the registration form data
#     #     username = request.POST['username']
#     #     email = request.POST['email']
#     #     phone = request.POST['phone']
#     #     password = request.POST['pass']
#     #     confirm_password = request.POST['cpass']
#     #     role = CustomUser.PATIENT  # Set the user role as needed

#     #     if username and email and phone and password and role:
#     #         if CustomUser.objects.filter(email=email).exists():
#     #             error_message = "Email is already registered."
#     #         elif password != confirm_password:
#     #             error_message = "Passwords do not match."
#     #         else:
#     #             # Create a new user
#     #             user = CustomUser(username=username, email=email, phone=phone, role=role)
#     #             user.set_password(password)  # Set the password securely
#     #             user.save()
#     #             # You may want to activate the user's account here or send a confirmation email
#     #             return redirect('login')
#     #     else:
#     #         error_message = "All fields are required."

#     #     return render(request, 'registerUser.html', {'error_message': error_message})

#     # Handle GET request to render the registration form
#     return render(request, 'registerUser.html')

# def login_user(request):
#     if request.method =='POST':
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('/userhome')
#         else:
#             messages.success(request,("there was an error"))
#             return redirect('/login')
#     else:
#         return render(request, 'login.html')
# def logout_user(request):
#     logout(request)
#     messages.success(request,("Logged out"))
#     return  redirect('userhome')

#seller Registration

def sellerreg(request):
    if request.method == 'POST':
        shop_name = request.POST.get('shopName')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')
        phone = request.POST.get('phoneNumber')
        shop_address = request.POST.get('shopAddress')
        tax_id = request.POST.get('taxIdentificationNumber')

        # Perform any additional validation here if needed

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
        elif CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
        else:
            user = CustomUser(
                user_types=CustomUser.SELLER,
                shop_name=shop_name,
                username=username,
                email=email,
                password=password,
                phone=phone,
                shop_address=shop_address,
                tax_id=tax_id,
            )
            user.set_password(password)
            user.save()
            messages.success(request, "Seller registered successfully.")
            return redirect('login')  # You can redirect to the login page or any other page

    return render(request, 'sellerreg.html')


# SELLER ADDING PRODUCTS SECTION
from django.shortcuts import render, redirect
from .models import Product, CustomUser
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@never_cache
@login_required
def add_product(request):
    if request.method == 'POST':
        product_name = request.POST['product_name']
        product_description = request.POST['product_description']
        category = request.POST['category']
        sub_category = request.POST['sub_category']
        brand = request.POST['brand']
        age = request.POST['age']
        material = request.POST['material']
        price = request.POST['price']
        gender = request.POST['gender']
        seller_id = request.user.id  # Use the currently logged-in seller's ID
        stock_quantity = request.POST['stock_quantity']
        status = request.POST['status']
        product_image = request.FILES['product_image']

        seller = CustomUser.objects.get(id=seller_id)  # Get the seller using their ID

        product = Product(
            name=product_name,
            description=product_description,
            category_id=category,
            sub_category_id=sub_category,
            brand_id=brand,
            age_id=age,
            material=material,
            price=price,
            gender=gender,
            seller=seller,
            quantity = stock_quantity,
            status=status,
            product_image=product_image,
        )

        product.save()
        # You can add any additional logic here (e.g., sending a confirmation email)
        return HttpResponse('Product added successfully')  # You can customize the response as needed

    sellers = CustomUser.objects.filter(user_types=CustomUser.SELLER)  # Filter sellers based on user_types
    category=Category.objects.all()
    sub=Subcategory.objects.all()
    context = {'sellers': sellers ,'category':category,'sub':sub}
    return render(request, 'add_product.html', context)


# 
# ...



    





# def product_list(request):
#     products = Product.objects.all()
#     return render(request, 'product_list.html', {'products': products})

# new
# from django.shortcuts import render, get_object_or_404
# from .models import Product, Category, Subcategory

def product_list(request, category_slug=None, subcategory_slug=None):
    # Fetch all products
    products = Product.objects.all()

    # Fetch all categories and subcategories
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()

    # Filtering by category
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    # Filtering by subcategory
    if subcategory_slug:
        subcategory = get_object_or_404(Subcategory, slug=subcategory_slug)
        products = products.filter(sub_category=subcategory)

    return render(request, 'product_list.html', {'products': products, 'categories': categories, 'subcategories': subcategories})

from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def product_list_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'product_list_by_category.html', {'category': category, 'products': products})




#seller editing products
from django.shortcuts import render, get_object_or_404, redirect,reverse
from .models import Product  # Import your Product model

def edit_product(request, product_id):
    # Get the product object to edit
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        # Handle the form submission and update the product
        product_name = request.POST.get('product_name')
        product_description = request.POST.get('product_description')
        category = request.POST.get('category')
        sub_category = request.POST.get('sub_category')
        brand = request.POST.get('brand')
        # material = request.POST.get('material')
        price = request.POST.get('price')
        age = request.POST.get('age')
        # seller = request.POST.get('seller')
        stock_quantity = request.POST.get('stock_quantity')
        # status = request.POST.get('status')

        # Update the product attributes
        product.name = product_name
        product.description = product_description
        product.Category = category
        product.Sub_category = sub_category
        product.Brand = brand
        # product.material = material
        product.price = price
        product.Age = age
        # product.seller = seller
        product.stock_quantity = stock_quantity
        # product.status = status

        if 'product_image' in request.FILES:
            product_image = request.FILES['product_image']

        # Save the changes
        product.save()

        # Redirect to a success page or wherever you want
        return redirect('view_product')

    sellers = CustomUser.objects.filter(user_types=CustomUser.SELLER)  # Filter sellers based on user_types
    category=Category.objects.all()
    sub=Subcategory.objects.all()
    context = {'sellers': sellers ,'category':category,'sub':sub}

    # Render the edit product form
    return render(request, 'edit_product.html', {'product': product})




def deactivate_product(request):
    return render(request, 'deactivate_product.html')


@login_required
def view_product(request):
    # Query the seller's products from the database
    seller = request.user  # Assuming the seller is a logged-in user
    seller_products = Product.objects.filter(seller=seller)

    return render(request, 'view_product.html', {'seller_products': seller_products})
#linnus add product and wishlist
def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    # Implement your cart functionality here (e.g., store in session or a database table)
    return redirect('cart')

def add_to_wishlist(request, product_id):
    product = Product.objects.get(pk=product_id)
    # Implement your wishlist functionality here (e.g., store in session or a database table)
    return redirect('wishlist')
def cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Retrieve cart items associated with the user's cart
    cart_items = CartItem.objects.filter(cart=cart)
    for item in cart_items:
        item.total_price = item.product.price * item.quantity
    
    total_amount = sum(item.total_price for item in cart_items)

    return render(request, 'cart.html', {'cart_items': cart_items,'total_amount': total_amount})
    
# @login_required
# def add_to_wishlist(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     # Get or create the user's wishlist
#     wishlist, created = WishlistItem.objects.get_or_create(user=request.user, product=product)
#     return HttpResponseRedirect(reverse('wishlist'))


# try
# views.py

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Product, WishlistItem

@csrf_exempt  # Add this decorator to disable CSRF protection for simplicity (you might want to handle CSRF properly in production)
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user

    # Check if the product is already in the wishlist
    if WishlistItem.objects.filter(user=user, product=product).exists():
        return JsonResponse({'message': 'This product is already added to your wishlist.'})
    
    # If not, add the product to the wishlist
    WishlistItem.objects.create(user=user, product=product)
    return JsonResponse({'message': 'Product added to your wishlist successfully.'})


def wishlist(request):
    # Get the wishlist items for the currently logged-in user
    wishlist_items = WishlistItem.objects.filter(user=request.user)

    # Pass the wishlist_items to the template
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})

@login_required
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    # Remove the product from the user's wishlist
    WishlistItem.objects.filter(user=request.user, product=product).delete()
    # Return a JSON response with a success message
    # return JsonResponse({'message': 'Product removed from your wishlist successfully.'})
    # return JsonResponse({'success': True, 'message': 'Product removed from your wishlist successfully.'})

    return redirect('wishlist')

def product_details(request, product_id):
    # Get the product by its ID, or return a 404 error if not found
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        # Your logic to handle Add to Cart or Add to Wishlist actions
        # ...

        # Get the message you want to display in the popup
        popup_message = "Product added to cart successfully."  # You can customize this message

        # Pass the popup message to the template
        return render(request, 'product_details.html', {'product': product, 'popup_message': popup_message})

    return render(request, 'product_details.html', {'product': product})



def userprofile(request):
    return render(request, 'userprofile.html')

def changepassword(request):
    return render(request, 'changepassword.html')


def shop(request):
    return render(request, 'shop.html')

def base(request):
    return render(request, 'base.html')

def navbar(request):
    return render(request, 'navbar.html')

def account(request):
    return render(request, 'account.html')
    

#add to cart
from .models import Product, Cart, CartItem
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

@login_required(login_url='login')
def add_to_cart(request, id):
    product = Product.objects.get(pk=id)  # Use correct model name 'Product'
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

    # Check if the product is already in the cart
    if product_already_added_to_cart:
        return JsonResponse({'message': 'This product is already added to your cart.'})
    else:
        return JsonResponse({'message': 'Product added to your cart successfully.'})


    
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('cart')

# Replace this function with your actual logic to check if the product is in the cart
def product_already_added_to_cart(request, product_id):
    # Your logic to check if the product is in the cart goes here
    # Return True if the product is in the cart, else return False
    pass


#remove from cart
@login_required(login_url='login')
def remove_from_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    cart = Cart.objects.get(user=request.user)
    try:
        cart_item = cart.cartitem_set.get(product=product)
        if cart_item.quantity >= 1:
             cart_item.delete()
             messages.success(request, 'Product removed from cart successfully.')
    except CartItem.DoesNotExist:
        pass
    
    return redirect('cart')

#view cart
# @login_required(login_url='login')
# def view_cart(request):
#     cart = request.user.cart
#     cart_items = CartItem.objects.filter(cart=cart)
#     return render(request, 'cart.html', {'cart_items': cart_items})

@login_required(login_url='login')
def view_cart(request):
    # Get or create the user's cart
    cart, created = Cart1.objects.get_or_create(user=request.user)

    # Retrieve cart items associated with the user's cart
    cart_items = CartItem1.objects.filter(cart=cart)
    for item in cart_items:
        item.total_price = item.product.price * item.quantity
    
    total_amount = sum(item.total_price for item in cart_items)

    return render(request, 'cart.html', {'cart_items': cart_items,'total_amount': total_amount})


#increase the cart and decrease the cart
@login_required(login_url='login')
def increase_cart_item(request, product_id):
    product = Product.objects.get(pk=product_id)
    cart = request.user.cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    cart_item.quantity += 1
    cart_item.save()

    return redirect('cart')

@login_required(login_url='login')
def decrease_cart_item(request, product_id):
    product = Product.objects.get(pk=product_id)
    cart = request.user.cart
    cart_item = cart.cartitem_set.get(product=product)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart')


#fetch_cart_count and get_cart_count
@login_required(login_url='login')
def fetch_cart_count(request):
    cart_count = 0
    if request.user.is_authenticated:
        cart = request.user.cart
        cart_count = CartItem.objects.filter(cart=cart).count()
    return JsonResponse({'cart_count': cart_count})

def get_cart_count(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(cart=request.user.cart)
        cart_count = cart_items.count()
    else:
        cart_count = 0
    return cart_count



# user_profile
def save_profile(request):
    return render(request, 'account.html')



#payment
# from .models import Profile, Product, Cart, CartItem, Order, OrderItem
from .models import  Product, Cart, CartItem, Order, OrderItem
from django.http import JsonResponse
from django.conf import settings
import razorpay
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create_order(request):
    if request.method == 'POST':
        user = request.user
        cart = user.cart

        cart_items = CartItem.objects.filter(cart=cart)
        total_amount = sum(item.product.price * item.quantity for item in cart_items)

        try:
            order = Order.objects.create(user=user, total_amount=total_amount)
            for cart_item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.quantity,
                    item_total=cart_item.product.price * cart_item.quantity
                )

            client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
            payment_data = {
                'amount': int(total_amount * 100),
                'currency': 'INR',
                'receipt': f'order_{order.id}',
                'payment_capture': '1'
            }
            # orderData = client.order.create(data=payment_data)
            orderData = client.order.create(data=payment_data)
            print(orderData)  # Add this line to log the order creation response

            order.payment_id = orderData['id']
            order.save()

            return JsonResponse({'order_id': orderData['id']})
        
        except Exception as e:
            print(str(e))
            return JsonResponse({'error': 'An error occurred. Please try again.'}, status=500)

#checkout
def checkout(request):
    cart_items = CartItem.objects.filter(cart=request.user.cart)
    total_amount = sum(item.product.price * item.quantity for item in cart_items)

    cart_count = get_cart_count(request)
    email = request.user.email
    # full_name = request.user.profile.full_name

    context = {
        'cart_count': cart_count,
        'cart_items': cart_items,
        'total_amount': total_amount,
        'email':email,
        # 'full_name': full_name
    }
    return render(request, 'checkout.html', context)



@csrf_exempt
def handle_payment(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        razorpay_order_id = data.get('order_id')
        payment_id = data.get('payment_id')

        try:
            order = Order.objects.get(payment_id=razorpay_order_id)

            client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
            payment = client.payment.fetch(payment_id)

            if payment['status'] == 'captured':
                order.payment_status = True
                order.save()
                # user = request.user
                # user.cart.cartitem_set.all().delete()
                return JsonResponse({'message': 'Payment successful'})
            else:
                return JsonResponse({'message': 'Payment failed'})

        except Order.DoesNotExist:
            return JsonResponse({'message': 'Invalid Order ID'})
        except Exception as e:

            print(str(e))
            return JsonResponse({'message': 'Server error, please try again later.'})


# filter by category
# views.py

from django.shortcuts import render
from django.views.generic import ListView
from .models import Category, Product

class ProductListView(ListView):
    model = Product
    template_name = 'your_app/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        subcategory_slug = self.kwargs.get('subcategory_slug')
        
        if subcategory_slug:
            subcategory = Subcategory.objects.get(slug=subcategory_slug)
            category_name = f"{subcategory.category.name} - {subcategory.name}"
            return subcategory.get_related_products(), category_name
        elif category_slug:
            category = Category.objects.get(slug=category_slug)
            return category.get_related_products(), category.name
        else:
            return Product.objects.all(), "All Products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['category_name'] = self.get_queryset()[1]  # Add category name to the context
        return context

# filter
from django.shortcuts import render
from .models import Product, Category, Subcategory, Brand, Age

def product_list(request):
    # Get all products
    products = Product.objects.all()

    # Get filter parameters from the request
    category_id = request.GET.get('category')
    subcategory_id = request.GET.get('subcategory')
    brand_id = request.GET.get('brand')
    age_id = request.GET.get('age')

    # Filter products based on parameters
    if category_id:
        filtered_category = Category.objects.get(id=category_id)
        products = products.filter(category_id=category_id)
    else:
        filtered_category = None

    if subcategory_id:
        products = products.filter(sub_category_id=subcategory_id)
    if brand_id:
        products = products.filter(brand_id=brand_id)
    if age_id:
        products = products.filter(age_id=age_id)

    # Retrieve all categories, subcategories, brands, and ages for the filter form
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    brands = Brand.objects.all()
    ages = Age.objects.all()

    context = {
        'products': products,
        'categories': categories,
        'subcategories': subcategories,
        'brands': brands,
        'ages': ages,
        'filtered_category': filtered_category,
        'filtered_products': products,
    }

    return render(request, 'product_list.html', context)


    #billinvoice
    # def bill_invoice(request):
    # Fetch the latest order for the logged-in user (or implement your logic)
        # order = Order.objects.filter(user=request.user).latest('created_at')
        # return render(request, 'billinvoice.html', {'order': order})
        

def bill_invoice(request):
# Fetch the latest order for the logged-in user (or implement your logic)
    order = Order.objects.filter(user=request.user).latest('created_at')
    return render(request, 'billinvoice.html', {'order': order})



