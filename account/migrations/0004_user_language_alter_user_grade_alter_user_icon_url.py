# Generated by Django 5.2 on 2025-04-07 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='language',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='grade',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='icon_url',
            field=models.TextField(default='defalut.jpg'),
        ),
    ]
