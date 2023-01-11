import datetime as dt
from django.utils.html import mark_safe
from django.db import models
from django.contrib.auth import get_user_model
from asgiref.sync import sync_to_async


PERMISSION_STATUS = (
    (True, 'Ishga tushirish'),
    (False, 'To\'xtatish'),
)


class TelegramUser(models.Model):
    full_name = models.CharField(
        max_length=100,
        verbose_name='Ismi va familiya'
    )

    username = models.CharField(
        max_length=40,
        verbose_name='Username',
        null=True,
        blank=True
    )

    tg_id = models.CharField(
        max_length=20,
        verbose_name='Telegram id'
    )

    chat_id = models.CharField(
        max_length=20,
        verbose_name='Chat id'
    )

    request_all_count = models.IntegerField(
        verbose_name='Umumiy so\'rovlar soni',
        default=0
    )

    def set_request_count(self):
        self.request_all_count += 1
        self.save()

    def __str__(self) -> str:
        return self.full_name

    def get_user(self):
        return self.user

    def set_user(self, user):
        self.user = user
        self.save()

    def get_username(self):
        return mark_safe(f"<a href='https://t.me/{self.username}'>@{self.username}</a>")


class Example(models.Model):
    description = models.TextField(
        verbose_name="Rasm haqida batafsil"
    )

    image = models.ImageField(
        upload_to='example/',
        verbose_name="Namuna rasm"
    )

    create_date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Example photo'
        verbose_name_plural = 'Example photos'


class Permission(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Ruhsat nomi'
    )

    permission_status = models.BooleanField(
        default=True,
        choices=PERMISSION_STATUS,
        verbose_name='Xolat'
    )

    def __str__(self):
        return self.name


class Request(models.Model):
    user = models.ForeignKey(
        to=TelegramUser,
        on_delete=models.SET_NULL,
        verbose_name='User',
        null=True,
        blank=True
    )

    create_add = models.DateTimeField(
        auto_now_add=True,
    )

    def get_date(self):
        return self.create_add.strftime("%H:%M:%S, %d/%m/%Y")


class Message(models.Model):
    user = models.ForeignKey(
        to=TelegramUser,
        on_delete=models.SET_NULL,
        verbose_name='User',
        null=True,
        blank=True
    )

    message = models.TextField(
        verbose_name='Xabar',
        blank=True,
        null=True
    )

    create_add = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.user} || {self.id} message'

    def get_message(self):
        return self.message[:100]

    def get_date(self):
        return self.create_add.strftime("%H:%M:%S, %d/%m/%Y")

    def get_username(self):
        return self.user.get_username
