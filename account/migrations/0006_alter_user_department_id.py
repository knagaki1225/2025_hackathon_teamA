# Generated by Django 4.2 on 2025-04-09 00:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0007_review_class_id'),
        ('account', '0005_user_admin_flg_user_career_user_create_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='department_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='review.department'),
        ),
    ]
