# Generated by Django 3.2.2 on 2021-05-20 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('phone', models.IntegerField(default='', max_length=12)),
                ('email', models.CharField(default='', max_length=30)),
                ('message', models.CharField(max_length=5000)),
            ],
        ),
    ]
