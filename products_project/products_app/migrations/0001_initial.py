# Generated by Django 4.2.9 on 2024-01-03 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=20)),
                ('product_name', models.CharField(max_length=50)),
                ('product_category', models.CharField(max_length=50)),
                ('product_price', models.FloatField()),
                ('product_expiry_date', models.CharField(max_length=20)),
                ('product_manufacturing_date', models.DateField()),
                ('product_hsn_no', models.CharField(max_length=8)),
                ('product_quantity', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ['product_category'],
            },
        ),
    ]
