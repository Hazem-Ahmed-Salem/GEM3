from django.contrib import admin 
from .models import User 
# from .forms import UserAdminCreationForm ,UserAdminChangeForm
from django.contrib.auth.models import Group


class UserAdmin(admin.ModelAdmin):
    
    

   
    readonly_fields =['date_joined','last_login','password']
    list_display = ['email', 'superuser','staff','active']
    list_filter = ['superuser','staff','active']
    fieldsets = (
        ('credentials', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name','last_name',)}),
        ('Permissions', {'fields': ('superuser','staff','active')}),
        ('Date', {'fields': ('date_joined','last_login')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = ()


admin.site.register(User, UserAdmin)

