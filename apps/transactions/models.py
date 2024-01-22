from django.db import models
from apps.users.models import User
# from django.utils.translation import gettext as _
# Create your models here.

class Transactions(models.Model):
    from_user = models.ForeignKey(User,
        on_delete=models.CASCADE,
        related_name = 'from_user',
        verbose_name = 'От пользователя'
    )
    to_user = models.ForeignKey(User,
        on_delete = models.CASCADE, 
        related_name = 'to_user',
        verbose_name = 'К пользователю'
    )
    is_complated = models.BooleanField(
        default=False,
        verbose_name="Статус"
    )
    created_at = models.DateTimeField(
        auto_now_add = True,
        verbose_name = 'Дата создания'
    )
    amount = models.SmallIntegerField(
        verbose_name = 'Coins'
    )

    def __str__(self):
        return self.from_user

    class Meta:
        verbose_name = "История"
        verbose_name_plural = "Истории"
