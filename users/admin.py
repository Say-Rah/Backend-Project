from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id','email', 'username', 'first_name', 'last_name','is_admin', 'is_staff')
    search_fields = ('id','email','username', 'first_name', 'last_name')









# from django.contrib import admin
# from .models import CustomUser

# # Register your models here.

# @admin.register(CustomUser)
# class CustomUserAdmin(admin.ModelAdmin)
#     list_display = (' ', ' ')
#     search_fields = (' ', ' ')
# admin.site.register(CustomUser)
