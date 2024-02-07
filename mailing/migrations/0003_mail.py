# Generated by Django 5.0.1 on 2024-02-03 16:28

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0002_message'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название')),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='начало')),
                ('next_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='следующее')),
                ('end_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='конец')),
                ('interval', models.CharField(choices=[('once_a_day', 'once_a_day'), ('once_a_week', 'once_a_week'), ('once_a_month', 'once_a_month')], default='разовая', max_length=50, verbose_name='интервал')),
                ('status', models.BooleanField(choices=[('start', 'start'), ('finish', 'finish'), ('created', 'created')], max_length=50, verbose_name='статус')),
                ('is_active', models.BooleanField(default=True, verbose_name='действующая')),
                ('client', models.ManyToManyField(to='mailing.client', verbose_name='кому')),
                ('message', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mailing.message', verbose_name='сообщение')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='владелец рассылки')),
            ],
            options={
                'verbose_name': 'рассылка',
                'verbose_name_plural': 'рассылки',
            },
        ),
    ]
