# Generated by Django 2.2.3 on 2019-08-07 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('field_1', models.PositiveSmallIntegerField(blank=True, default=5, null=True)),
                ('field_2', models.CharField(blank=True, max_length=200)),
                ('field_3', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'ordering': ('created',),
                'get_latest_by': ('created',),
            },
        ),
    ]