# from django.contrib import admin

from .models import CustomUser
# Register your models here.
# admin.site.register(CustomUser)

# Register your models here.



# new
from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()

class SuperuserAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return User.objects.filter(is_superuser=False)

# Register the custom admin class
admin.site.register(User, SuperuserAdmin)