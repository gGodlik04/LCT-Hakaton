from django.db import models
import uuid
from django.conf import settings

from directories.models import TaskTypeModel, AgentPointModel
from .status import TaskStatusChoices, TaskPriorityChoices
'''class ObjectsTimeControl(models.Model):
    created_on = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Время изменения', auto_now=True)

    class Meta:
        abstract = True'''


class Task(models.Model):

    uuid = models.UUIDField('UUID', primary_key=True, default=uuid.uuid4, editable=False)
    appointment_date = models.DateField('Время начала задачи', null=True,)
    priority = models.PositiveSmallIntegerField('Приоритет', choices=TaskPriorityChoices.choices, null=True)
    status = models.PositiveSmallIntegerField('Статус задачи', choices=TaskStatusChoices.choices, default=1)
    comment = models.TextField('Коментарий к задаче', null=True)
    favorite = models.BooleanField('Избранное?', default=False)
     
    agent_point = models.ForeignKey(AgentPointModel, on_delete=models.DO_NOTHING)
    task_type = models.ForeignKey(TaskTypeModel, on_delete=models.DO_NOTHING)
    employee = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.DO_NOTHING, null=True)
    
    class Meta:
        verbose_name = 'Задачи'
        db_table = "Task"



