# Generated by Django 5.0.4 on 2024-04-16 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='icon',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='image_1',
            field=models.ImageField(upload_to='logo/'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='image_2',
            field=models.ImageField(upload_to='logo/'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='image_3',
            field=models.ImageField(upload_to='logo/'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='image_about',
            field=models.ImageField(upload_to='logo/'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='image_blog',
            field=models.ImageField(upload_to='logo/'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='image_contact',
            field=models.ImageField(upload_to='logo/'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='image_product',
            field=models.ImageField(upload_to='logo/'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='logo',
            field=models.ImageField(upload_to='logo/'),
        ),
    ]
