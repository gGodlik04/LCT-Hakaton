from django.db import models
import uuid
from django.conf import settings

from .status import TaskStatusChoices
'''class ObjectsTimeControl(models.Model):
    created_on = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Время изменения', auto_now=True)

    class Meta:
        abstract = True'''


class Task(models.Model):

    uuid = models.UUIDField('UUID', primary_key=True, default=uuid.uuid4, editable=False)
    agent_point_date = models.CharField('Дата подключения точки', max_length=50, null=False)
    materials = models.BooleanField('Материалы доставлены', null=False, )
    last_card_given = models.DateField('Дата последней выдачи карты',  null=True)
    num_given_cards = models.SmallIntegerField('Выданные карты', null=False,)
    approved_requests = models.SmallIntegerField('Одобренные заявки', null=False,)
    priority = models.SmallIntegerField('Приоритет', null=True)
    address = models.CharField('Адрес', max_length=255,)
    work_time = models.SmallIntegerField('Время на выполнение', null=False,)
    appointment_date = models.DateField('Время начала задачи', null=True,)
    status = models.PositiveSmallIntegerField('Статус задачи', choices=TaskStatusChoices.choices, default=1)
    task_type = models.CharField('Тип задачи', max_length=50, null=False)
    comment = models.TextField('Коментарий к задаче', null=True)
    favorite = models.BooleanField('Избранное', null=True, default=False)

    employee = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='employee_task',
                                 on_delete=models.DO_NOTHING, null=True)
    
    class Meta:

        verbose_name = 'Задачи'
        db_table = "Task"



