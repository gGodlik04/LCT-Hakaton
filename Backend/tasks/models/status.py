from django.db import models


class TaskStatusChoices(models.IntegerChoices):
    APPOINTED = 1
    ON_THE_WAY = 2
    IN_WORK = 3
    FINISH = 4
