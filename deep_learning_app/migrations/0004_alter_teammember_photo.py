# Generated by Django 4.2.4 on 2023-12-13 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deep_learning_app', '0003_alter_teammember_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='photo',
            field=models.ImageField(default='deep_learning_app/static/default-user.png', upload_to='deep_learning_app/static/team_photos/'),
        ),
    ]