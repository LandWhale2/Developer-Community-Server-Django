# Generated by Django 2.2.9 on 2020-01-02 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='skills',
            field=models.CharField(max_length=255, null=True),
        ),
    ]