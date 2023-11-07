from django.db import models


class UserRoleChoices(models.IntegerChoices):
    MANAGER = 1, 'Тимлид-менеджер'
    EMPLOYEE = 2, 'Выездной работник'
    ADMIN = 3, 'Администратор'
