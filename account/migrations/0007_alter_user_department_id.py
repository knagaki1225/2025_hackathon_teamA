# Generated by Django 4.2 on 2025-04-09 01:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0007_review_class_id'),
        ('account', '0006_alter_user_department_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='department_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='review.department'),
        ),
    ]
