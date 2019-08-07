from django.db import models
import uuid
from django.conf import settings

# User = settings.AUTH_USER_MODEL


# Create your models here.

class Inviter(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    number_for_invite = models.UUIDField(default=uuid.uuid4, max_length=13, help_text='реф номер для приглашений')
    user_number_for_invite = models.CharField(max_length=150, verbose_name='реф номер пригласителя')
    invited_link = models.CharField(max_length=100, verbose_name='ссылка на того, кто пригласил')

    class Meta:
        abstract = True



class Driver(Inviter):
    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='фамилия')
    lastname = models.CharField(max_length=50, verbose_name='отчество')
    phone = models.CharField(max_length=15, verbose_name='телефон', blank=True, null=True)
    balance = models.CharField(max_length=150, verbose_name='баланс', blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    def __str__(self):
        return self.user.name


class Car(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, verbose_name='car_driver')
    number = models.CharField(max_length=15, verbose_name='номер автомобиля')
    car_mark = models.CharField(max_length=30, verbose_name='марка автомобиля')
    car_model = models.CharField(max_length=50, verbose_name='модель автомобиля')

    class Meta:
        ordering = ["number"]
        verbose_name = "автомобиль"
        verbose_name_plural = "автомобили"

    def __str__(self):
        return self.number


class UserImage(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, verbose_name='img_driver')
    image = models.ImageField(upload_to='images/user/', )

    def save(self, *args, **kwargs):
        qs = UserImage.objects.count()
        if qs > 7:
            qs[0].delete()