# Generated by Django 5.0.2 on 2024-02-29 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_products_prod_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=100)),
                ('l_name', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=250)),
                ('email_id', models.EmailField(max_length=250)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
