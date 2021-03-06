# Generated by Django 3.2.8 on 2021-10-21 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='국가명')),
                ('date', models.DateTimeField(max_length=10, verbose_name='시행날짜')),
                ('imgUrl', models.CharField(max_length=100, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.CharField(max_length=10, verbose_name='단계')),
                ('comment', models.CharField(max_length=500, verbose_name='추가설명')),
                ('product_id', models.ForeignKey(db_column='product_id', on_delete=django.db.models.deletion.CASCADE, related_name='product_id', to='localstatus.product')),
            ],
        ),
    ]
