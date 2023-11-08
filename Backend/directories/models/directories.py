from django.db import models
from .choices import PointDate, TaskPriority, GradeChoices
import uuid


class AgentPointModel(models.Model):

    uuid = models.UUIDField('UUID', primary_key=True, default=uuid.uuid4, editable=False)
    address = models.CharField('Адрес точки', max_length=255, )
    agent_point_date = models.CharField('Дата подключения точки', choices=PointDate.choices, max_length=25, null=False)
    materials = models.BooleanField('Материалы доставлены', null=False,)
    last_card_given = models.DateField('Дата последней выдачи карты', null=True)
    num_given_cards = models.SmallIntegerField('Выданные карты',)
    approved_requests = models.SmallIntegerField('Одобренные заявки',)
    last_deliver = models.DateField('Последняя доставка материала',)
    last_teaching = models.DateField('Последнее проведение обуччения',)
    last_stimulation = models.DateField('Последняя стимуляция выдач',)

    class Meta:
        db_table = "AgentPoint"
        verbose_name = 'Агентские точки'
        verbose_name_plural = 'Агентские точки'


class TaskTypeModel(models.Model):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('Название типа задач', max_length=128, null=False)
    priority = models.PositiveSmallIntegerField('Приоритет задачи', choices=TaskPriority.choices, null=False)
    work_time = models.PositiveSmallIntegerField('Время выполнения', )
    condition_1 = models.CharField('Условие 1', max_length=256, null=False)
    condition_2 = models.CharField('Условие 2', max_length=256)
    grade = models.PositiveSmallIntegerField('Нужный грейд', choices=GradeChoices.choices, null=False)

    class Meta:
        db_table = "TaskType"
        verbose_name = 'Тип задач'
        verbose_name_plural = 'Тип задач'
