from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db.models.query import QuerySet
from django.http import HttpRequest

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User, StaffSchedule


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'name', 'address',  'is_active','is_staff')
    list_filter = ('email', 'name', 'address',  'is_active','is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'name', 'address', 'password')}),
        # ('Permissions', {'fields': ('is_active', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'address', 'password1', 'password2', 'is_active', 'is_staff')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email','name')
    def get_queryset(self, request: HttpRequest) -> QuerySet:
        if request.user.is_superuser or request.user.is_staff:
            return User.objects.filter(is_superuser=False)
        

admin.site.register(User, CustomUserAdmin)
admin.site.register(StaffSchedule)