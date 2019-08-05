from django.db import models

# Create your models here.

class Inviter(models.Model):
    number_for_invite = models.IntegerField(verbose_name='реф номер для приглашений')
    user_number_for_invite = models.IntegerField(verbose_name='реф номер пригласителя')
    invited_link = models.CharField(verbose_name='ссылка на того, кто пригласил', max_length=50)

    class Meta:
        abstract = True



class User(Inviter):
    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='фамилия')
    lastname = models.CharField(max_length=50, verbose_name='отчество')
    phone = models.SmallIntegerField(verbose_name='телефон', blank=True, null=True)
    balance = models.CharField(max_length=50, verbose_name='баланс', blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    def __str__(self):
        return self.name


class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='car_driver')
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='img_driver')
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='images/', )

    def __str__(self):
        return self.title