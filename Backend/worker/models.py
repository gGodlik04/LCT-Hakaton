from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser



class Task(models.Model):

    uuid = models.UUIDField('UUID', primary_key=True, default=uuid.uuid4, editable=False)
    agent_point_date = models.CharField('Дата подключения точки', max_length=50)
    materials = models.BooleanField('Материалы доставлены')
    last_card_given = models.SmallIntegerField('Дата последней выдачи карты')
    num_given_cards = models.SmallIntegerField('Выданные карты')
    approved_requests = models.SmallIntegerField('Одобренные заявки')
    employee = models.BigIntegerField('Исполнитель задания')
    priority = models.SmallIntegerField('Приоритет', )
    address = models.CharField('Адрес', max_length=255, default='Dagestanskaya')
    work_time = models.SmallIntegerField('Время на выполнение')
    appointment_date = models.DateField('Время начала задачи', null=True)
    status = models.SmallIntegerField('Статус задачи')
    task_type = models.CharField('Тип задачи', max_length=50)

    class Meta:
        permissions = [
            ('create_task', 'Can create task'),
            ('close_task', 'Can close task'),
        ],
        verbose_name = 'Задачи'


