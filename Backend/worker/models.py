from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser


class Task(models.Model):

    uuid = models.UUIDField('UUID', primary_key=True, default=uuid.uuid4, editable=False)
    agent_point_date = models.CharField('Дата подключения точки', max_length=50, default='Недавно', null=False)
    materials = models.BooleanField('Материалы доставлены', null=False, default=True)
    last_card_given = models.DateField('Дата последней выдачи карты', default='2000-01-01', null=False)
    num_given_cards = models.SmallIntegerField('Выданные карты', null=False, default=8)
    approved_requests = models.SmallIntegerField('Одобренные заявки', null=False, default=10)
    employee = models.BigIntegerField('Исполнитель задания', null=True)
    priority = models.SmallIntegerField('Приоритет', null=True)
    address = models.CharField('Адрес', max_length=255, default='Dagestanskaya')
    work_time = models.SmallIntegerField('Время на выполнение', null=False, default=2)
    appointment_date = models.DateField('Время начала задачи', null=True, default='2000-01-01')
    status = models.SmallIntegerField('Статус задачи', default=1, null=True)
    task_type = models.CharField('Тип задачи', max_length=50, default='Забрать карта', null=False)

    class Meta:
        permissions = [
            ('create_task', 'Can create task'),
            ('close_task', 'Can close task'),
        ],
        verbose_name = 'Задачи'


