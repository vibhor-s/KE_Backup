# Generated by Django 3.2.2 on 2021-05-21 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_product_display_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='prod_img1',
            field=models.ImageField(blank=True, default='', null=True, upload_to='shop/images'),
        ),
        migrations.AddField(
            model_name='product',
            name='prod_img2',
            field=models.ImageField(blank=True, default='', null=True, upload_to='shop/images'),
        ),
        migrations.AddField(
            model_name='product',
            name='prod_img3',
            field=models.ImageField(blank=True, default='', null=True, upload_to='shop/images'),
        ),
        migrations.AddField(
            model_name='product',
            name='prod_img4',
            field=models.ImageField(blank=True, default='', null=True, upload_to='shop/images'),
        ),
        migrations.AddField(
            model_name='product',
            name='prod_img5',
            field=models.ImageField(blank=True, default='', null=True, upload_to='shop/images'),
        ),
        migrations.AddField(
            model_name='product',
            name='prod_img6',
            field=models.ImageField(blank=True, default='', null=True, upload_to='shop/images'),
        ),
        migrations.AddField(
            model_name='product',
            name='prod_img7',
            field=models.ImageField(blank=True, default='', null=True, upload_to='shop/images'),
        ),
        migrations.AddField(
            model_name='product',
            name='prod_img8',
            field=models.ImageField(blank=True, default='', null=True, upload_to='shop/images'),
        ),
    ]
