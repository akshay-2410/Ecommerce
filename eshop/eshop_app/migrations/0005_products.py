# Generated by Django 5.0.6 on 2024-08-22 13:48

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_app', '0004_remove_categories_image_subcatg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('image_product', models.ImageField(null=True, upload_to='images/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('subcategory', models.ManyToManyField(blank=True, to='eshop_app.subcategories')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
