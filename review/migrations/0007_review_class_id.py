# Generated by Django 5.2 on 2025-04-08 01:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0006_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='class_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='review.class'),
            preserve_default=False,
        ),
    ]
