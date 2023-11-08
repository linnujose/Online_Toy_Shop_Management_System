
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static  import static

urlpatterns = [
   path('',views.index,name="index"),
   
   path('login/',views.login,name="login"),
   path('register/',views.register,name="register"),
   path('logout/',views.logout_view,name="logout"),
   path('userhome/',views.userhome,name="userhome"),
   path('sellerreg/',views.sellerreg,name="sellerreg"),
   path('sellerhome/',views.sellerhome,name="sellerhome"),
   path('add_product/',views.add_product,name="add_product"),
   path('view_product/',views.view_product,name="view_product"),
   path('product_list/',views.product_list,name="product_list"),
   path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
   path('deactivate_product/<int:product_id>/', views.deactivate_product, name='deactivate_product'),
   
   #linnus add to whislist and cart
   path('product/<int:product_id>/', views.product_details, name='product_details'),
   path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
   path('add_to_wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    
   path('cart/', views.cart, name='cart'),
   path('wishlist/', views.wishlist, name='wishlist'),
   path('remove_from_wishlist/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),


   
 
      # forgot password

   path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
   path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
   path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
   path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
