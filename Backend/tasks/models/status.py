from django.db import models


class TaskStatusChoices(models.IntegerChoices):
    APPOINTED = 1
    ON_THE_WAY = 2
    IN_WORK = 3
    FINISH = 4
    NOT_DONE = 5
    TOMORROW = 6
    ELSE = 7


class TaskTypeChoices(models.IntegerChoices):
    STIMULATION = 1
    TEACHING = 2
    DELIVERING = 3


