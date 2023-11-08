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


# def add_product(request):
#     sellers = CustomUser.objects.filter(user_types=4)  # Assuming you have a Seller model

#     if request.method == 'POST':
#         product_name = request.POST.get('product_name')
#         product_description = request.POST.get('product_description')
#         category_id = request.POST.get('category_id')  # Update the field name to match your HTML form
#         sub_category = request.POST.get('sub_category')
#         material = request.POST.get('material')
#         price = request.POST.get('price')
#         gender = request.POST.get('gender')
#         seller_id = request.POST.get('seller')
#         stock_quantity = request.POST.get('stock_quantity')
#         status = request.POST.get('status')
#         
#         brand = request.POST.get('brand')  # New field
#         age = request.POST.get('age')  # New field
#         product_image = request.FILES.get('product_image')  # New field

#         seller = CustomUser.objects.get(pk=seller_id, user_types=4)

#         category = Category.objects.get(pk=category_id)
#         subcategory = Subcategory.objects.get(name=sub_category)

#         product = Product(
#             product_name=product_name,
#             product_description=product_description,
#             category=category,
#             sub_category=subcategory,
#             material=material,
#             price=price,
#             gender=gender,
#             seller=seller,
#             stock_quantity=stock_quantity,
#             status=status,
#             discount=discount,
#             brand=brand,  # New field
#             age=age,  # New field
#             product_image=product_image  # New field
#         )
#         product.save()
#         return redirect('sellerhome')

#     return render(request, 'add_product.html', {'sellers': sellers})

# ...

# def add_product(request):
#     sellers = CustomUser.objects.filter(user_types=4)  # Assuming you have a Seller model
#     error_message = None

#     if request.method == 'POST':
#         product_name = request.POST.get('product_name')
#         product_description = request.POST.get('product_description')
#         category_id = request.POST.get('category_id')  # Update the field name to match your HTML form
#         sub_category = request.POST.get('sub_category')
#         material = request.POST.get('material')
#         price = request.POST.get('price')
#         gender = request.POST.get('gender')
#         seller_id = request.POST.get('seller')
#         stock_quantity = request.POST.get('stock_quantity')
#         status = request.POST.get('status')
#         discount = request.POST.get('discount')
#         brand = request.POST.get('brand')  # New field
#         age = request.POST.get('age')  # New field
#         product_image = request.FILES.get('product_image')  # New field

#         try:
#             seller = CustomUser.objects.get(pk=seller_id, user_types=4)
#         except CustomUser.DoesNotExist:
#             seller = None

#         if seller:
#             try:
#                 category = Category.objects.get(pk=category_id)  # Retrieve the Category instance based on the category_id
#                 product = Product(
#                     product_name=product_name,
#                     product_description=product_description,
#                     category=category,
#                     sub_category=sub_category,
#                     material=material,
#                     price=price,
#                     gender=gender,
#                     seller=seller,
#                     stock_quantity=stock_quantity,
#                     status=status,
#                     discount=discount,
#                     brand=brand,  # New field
#                     age=age,  # New field
#                     product_image=product_image  # New field
#                 )
#                 product.full_clean()  # Validate the model fields
#                 product.save()
#                 return redirect('sellerhome')  # Replace 'success' with the URL where you want to redirect after a successful form submission

#             except Category.DoesNotExist:
#                 error_message = "Invalid category selection."

#             except ValidationError as e:
#                 error_message = str(e)
#         else:
#             error_message = "Invalid seller."

#     return render(request, 'add_product.html', {'sellers': sellers, 'error_message': error_message})


    
# def add_product(request):
#     sellers = CustomUser.objects.filter(user_types=4)  # Assuming you have a Seller model
    
#     if request.method == 'POST':
#         product_name = request.POST.get('product_name')
#         product_description = request.POST.get('product_description')
#         category_id = request.POST.get('category')
        
#         sub_category = request.POST.get('sub_category')
#         material = request.POST.get('material')
#         price = request.POST.get('price')
#         gender = request.POST.get('gender')
#         seller_id = request.POST.get('seller')
#         stock_quantity = request.POST.get('stock_quantity')
#         status = request.POST.get('status')
#         discount = request.POST.get('discount')
#         brand = request.POST.get('brand')  # New field
#         age = request.POST.get('age')  # New field
#         product_image = request.FILES.get('product_image')  # New field

#         try:
#             seller = CustomUser.objects.get(pk=seller_id, user_types=4)
#         except CustomUser.DoesNotExist:
#             seller = None

#         if seller:
#             try:
#                 category = Category.objects.get(pk=category_id)  # Retrieve the Category instance based on the category_id
#                 product = Product(
#                     product_name=product_name,
#                     product_description=product_description,
#                     category=category,
#                     sub_category=sub_category,
#                     material=material,
#                     price=price,
#                     gender=gender,
#                     seller=seller,
#                     stock_quantity=stock_quantity,
#                     status=status,
#                     discount=discount,
#                     brand=brand,  # New field
#                     age=age,  # New field
#                     product_image=product_image  # New field
#                 )
#                 product.full_clean()  # Validate the model fields
#                 product.save()
#                 return redirect('sellerhome')  # Replace 'success' with the URL where you want to redirect after a successful form submission

#             except Category.DoesNotExist:
#                 error_message = "Invalid category."

                
#             except ValidationError as e:
#                 error_message = str(e)
#         else:
#             error_message = "Invalid seller."

#     else:
#         error_message = None

#     return render(request, 'add_product.html', {'sellers': sellers, 'error_message': error_message})





def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

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
    # Logic to display cart items, if any
    return render(request, 'cart.html')
@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    # Get or create the user's wishlist
    wishlist, created = WishlistItem.objects.get_or_create(user=request.user, product=product)
    return HttpResponseRedirect(reverse('wishlist'))

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
    return redirect('wishlist')

def product_details(request, product_id):
    # Get the product by its ID, or return a 404 error if not found
    product = get_object_or_404(Product, id=product_id)

    return render(request, 'product_details.html', {'product': product})






