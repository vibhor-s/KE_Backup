# Generated by Django 3.2.2 on 2021-05-31 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20210521_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='icons',
            fields=[
                ('icon_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('icon_category', models.CharField(default='', max_length=100)),
                ('icon_img', models.ImageField(blank=True, default='', null=True, upload_to='shop/icons')),
            ],
        ),
    ]