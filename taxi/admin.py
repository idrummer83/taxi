from django.contrib import admin

# Register your models here.

from .models import User, UserImage, Car


class AdminUserImage(admin.TabularInline):
    model = UserImage


class AdminCar(admin.TabularInline):
    model = Car


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'lastname', 'phone', 'balance')
    inlines = [
        AdminCar, AdminUserImage
    ]