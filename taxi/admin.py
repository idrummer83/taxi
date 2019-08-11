from django.contrib import admin
from tabbed_admin import TabbedModelAdmin
from django.conf import settings

User = settings.AUTH_USER_MODEL
# Register your models here.

from taxi.models import Driver, UserImage, Car


class AdminUserImage(admin.TabularInline):
    model = UserImage


class AdminCar(admin.TabularInline):
    model = Car


@admin.register(Driver)
class AdminDriver(TabbedModelAdmin):
    list_display = ('id', 'name', 'surname', 'lastname')
    model = Driver
    tab_user = (
        (None, {
            'fields': ('number_for_invite', 'name', 'surname', 'lastname',
                       'phone', 'balance', 'user_number_for_invite')
        }),
    )
    tab_car = (
        AdminCar,
    )
    tab_image = (
        AdminUserImage,
    )
    tabs = [
        ('Пользователь', tab_user),
        ('Автомобиль', tab_car),
        ('Фото', tab_image)
    ]

