from django.db import models


class UserRoleChoices(models.IntegerChoices):
    MANAGER = 1
    EMPLOYEE = 2
    ADMIN = 3


class GradeChoices(models.IntegerChoices):
    JUNIOR = 1
    MIDDLE = 2
    SENIOR = 3



