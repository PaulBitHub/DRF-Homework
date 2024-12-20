from django.contrib.auth.models import AbstractUser
from django.db import models

from courses.models import Course, Lesson


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True, verbose_name="email", help_text="Укажите почту"
    )
    phone = models.CharField(
        max_length=35,
        verbose_name="phone_number",
        blank=True,
        null=True,
        help_text="Введите номер телефона",
    )
    city = models.CharField(
        max_length=100,
        verbose_name="city",
        blank=True,
        null=True,
        help_text="Введите страну",
    )
    avatar = models.ImageField(
        upload_to="users/avatars/",
        verbose_name="avatar",
        blank=True,
        null=True,
        help_text="Загрузите аватар",
    )

    token = models.CharField(
        max_length=100, verbose_name="token", blank=True, null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class Payment(models.Model):
    class TypeOfPay(models.TextChoices):
        CASH = "CASH", "CASH"
        CARD = "CARD", "CARD"

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="payments",
    )
    pay_date = models.DateField(verbose_name="дата оплаты")
    payed_course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        related_name="payments",
        blank=True,
        null=True,
    )
    payed_lesson = models.ForeignKey(
        Lesson,
        on_delete=models.SET_NULL,
        related_name="payments",
        blank=True,
        null=True,
    )
    payed_money = models.PositiveIntegerField(verbose_name="сумма оплаты")
    type_of_pay = models.CharField(
        max_length=5, choices=TypeOfPay.choices, verbose_name="способ оплаты"
    )

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        return f"{self.user} - {self.payed_money} ({self.pay_date})"
