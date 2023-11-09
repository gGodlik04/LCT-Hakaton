from django.db import models


class PointDate(models.TextChoices):
    LONG_TIME = 'давно'
    YESTERDAY = 'вчера'


class TaskPriority(models.IntegerChoices):
    LOW = 1
    MEDIUM = 2
    HIGH = 3


class GradeChoices(models.IntegerChoices):
    JUNIOR = 1
    MIDDLE = 2
    SENIOR = 3



