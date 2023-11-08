from django.db import models


class PointDate(models.TextChoices):
    LONG_TIME = 'long_ago'
    YESTERDAY = 'yesterday'


class TaskPriority(models.IntegerChoices):
    LOW = 1
    MEDIUM = 2
    HIGH = 3


class GradeChoices(models.IntegerChoices):
    JUNIOR = 1
    MIDDLE = 2
    SENIOR = 3



