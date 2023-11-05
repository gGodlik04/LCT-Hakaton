from django.db import models


class Task(models.Model):

    uuid = models.UUIDField('UUID', primary_key=True, editable=False)
    task_id = models.BigIntegerField()
    agent_point_date = models.CharField('Дата подключения точки', max_length=50)
    materials = models.BooleanField('Материалы доставлены')
    last_card_given = models.SmallIntegerField('Дата последней выдачи карты')
    num_given_cards = models.SmallIntegerField('Выданные карты')
    approved_requests = models.SmallIntegerField('Одобренные заявки')
    employee = models.BigIntegerField('Исполнитель задания')
    priority = models.SmallIntegerField('Приоритет', )
    slug = models.SlugField('URL', max_length=40,)


class Employee(models.Model):

    uuid = models.UUIDField('UUID', primary_key=True, editable=False)


