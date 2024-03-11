# Generated by Django 4.2.10 on 2024-03-09 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id_product', models.IntegerField()),
                ('Id_user', models.IntegerField()),
                ('price', models.FloatField()),
                ('qty', models.IntegerField()),
                ('tax', models.FloatField()),
                ('total', models.FloatField()),
                ('discount', models.FloatField()),
                ('net', models.FloatField()),
                ('status', models.BooleanField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ItemDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('qty', models.IntegerField()),
                ('tax', models.FloatField()),
                ('cata', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=500, null=True)),
                ('total', models.FloatField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('itemsid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.items')),
            ],
        ),
    ]
