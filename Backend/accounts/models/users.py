from django.db import models
from django.contrib.auth.models import AbstractUser
from .roles import UserRoleChoices


class User(AbstractUser):
    role = models.PositiveSmallIntegerField(verbose_name='Тип пользователя', choices=UserRoleChoices.choices)
    phone_number = models.CharField(max_length=32, verbose_name='Телефон пользователя')
    middle_name = models.CharField(max_length=100, verbose_name='Отчество')
    email = models.EmailField(max_length=255, verbose_name='Email пользователя', unique=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'role', 'password']
    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'

    def __repr__(self):
        return (
            f"role={self.role}, first_name={self.last_name},"
            f"last_name={self.last_name}, email={self.email},"
        )

    def __str__(self):
        return f"{self.username}"

    def is_manager_user(self):
        return self.role in UserRoleChoices.MANAGER

    def is_worker_user(self):
        return self.role in UserRoleChoices.EMPLOYEE

    def is_admin_user(self):
        return self.role in UserRoleChoices.ADMIN

