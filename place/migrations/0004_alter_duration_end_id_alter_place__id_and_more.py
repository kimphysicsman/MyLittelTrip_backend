# Generated by Django 4.0.6 on 2022-07-15 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0003_duration_end_id_duration_start_id_alter_place__id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duration',
            name='end_id',
            field=models.BigIntegerField(default=None, null=True, verbose_name='도착지 장소 id'),
        ),
        migrations.AlterField(
            model_name='place',
            name='_id',
            field=models.BigIntegerField(unique=True, verbose_name='장소 id'),
        ),
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(max_length=100, verbose_name='장소 이름'),
        ),
    ]
