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

from django.contrib.auth.decorators import login_required
#here
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return render(request, 'index.html')


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
                # elif request.user.user_typ == CustomUser.VENDOR:
                #     print("user is therapist")
                #     return redirect(reverse('therapist'))
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