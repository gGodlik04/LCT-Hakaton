from django.db import models


class UserRoleChoices(models.IntegerChoices):
    MANAGER = 1
    EMPLOYEE = 2
    ADMIN = 3

