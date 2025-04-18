# Generated by Django 5.2 on 2025-04-08 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0004_good_review_id_reply'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=20)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('del_flg', models.BooleanField(default=False)),
            ],
        ),
    ]
