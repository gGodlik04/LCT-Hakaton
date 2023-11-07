# Generated by Django 4.2.7 on 2023-11-06 15:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='UUID')),
                ('agent_point_date', models.CharField(max_length=50, verbose_name='Дата подключения точки')),
                ('materials', models.BooleanField(verbose_name='Материалы доставлены')),
                ('last_card_given', models.DateField(null=True, verbose_name='Дата последней выдачи карты')),
                ('num_given_cards', models.SmallIntegerField(verbose_name='Выданные карты')),
                ('approved_requests', models.SmallIntegerField(verbose_name='Одобренные заявки')),
                ('priority', models.SmallIntegerField(null=True, verbose_name='Приоритет')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('work_time', models.SmallIntegerField(verbose_name='Время на выполнение')),
                ('appointment_date', models.DateField(null=True, verbose_name='Время начала задачи')),
                ('status', models.SmallIntegerField(null=True, verbose_name='Статус задачи')),
                ('task_type', models.CharField(max_length=50, verbose_name='Тип задачи')),
                ('comment', models.TextField(null=True, verbose_name='Коментарий к задаче')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='employee_task', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Задачи',
                'db_table': 'Task',
            },
        ),
    ]