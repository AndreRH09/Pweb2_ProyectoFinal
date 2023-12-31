# Generated by Django 4.2.3 on 2023-07-28 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='comidas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tipo', models.CharField(choices=[('0', 'Otro'), ('1', 'Bebidas'), ('2', 'Postres'), ('3', 'Comidas')], default='4', max_length=2)),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.TextField(default='')),
                ('price', models.IntegerField()),
            ],
        ),
    ]
