from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    phone = models.CharField(
        max_length = 100,
        verbose_name = "Номер телефона"
    )
    age = models.PositiveIntegerField(
        verbose_name = "Возраст студента",
        blank =True, null = True
    )
    direction = models.CharField(
        max_length = 100,
        verbose_name = "Направление студента"
    )
    balance = models.IntegerField(
        verbose_name = "Баланс",
        default = 4,
        blank = True, null = True,
    )
    wallet_adress = models.CharField(
        max_length = 16,
        blank = True, null = True,
        unique = True,
        verbose_name = "Кошелек"
    )

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

