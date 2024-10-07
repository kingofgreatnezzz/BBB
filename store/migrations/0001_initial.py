# Generated by Django 5.0.6 on 2024-05-20 08:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=150)),
                ('product_img', models.ImageField(blank=True, null=True, upload_to=None)),
                ('product_category', models.CharField(blank=True, max_length=50, null=True)),
                ('product_info', models.TextField(blank=True, null=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('stock_count', models.IntegerField(blank=True, default=0, null=True)),
                ('createdat', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
