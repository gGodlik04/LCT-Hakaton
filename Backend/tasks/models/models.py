from django.db import models
import uuid
from django.conf import settings

from .status import TaskStatusChoices, TaskPriorityChoices
'''class ObjectsTimeControl(models.Model):
    created_on = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Время изменения', auto_now=True)

    class Meta:
        abstract = True'''


class Task(models.Model):

    uuid = models.UUIDField('UUID', primary_key=True, default=uuid.uuid4, editable=False)
    appointment_date = models.DateField('Время начала задачи', null=True,)
    priority = models.PositiveSmallIntegerField('Приоритет', choices=TaskPriorityChoices.choices, null=False)
    status = models.PositiveSmallIntegerField('Статус задачи', choices=TaskStatusChoices.choices, default=1)
    task_type = models.PositiveSmallIntegerField('Тип задачи', choices=TaskPriorityChoices.choices, null=False)
    comment = models.TextField('Коментарий к задаче', null=True)
    favorite = models.BooleanField('Избранное?', default=False)

    employee = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='employee_task',
                                 on_delete=models.DO_NOTHING, null=True)
    
    class Meta:

        verbose_name = 'Задачи'
        db_table = "Task"



