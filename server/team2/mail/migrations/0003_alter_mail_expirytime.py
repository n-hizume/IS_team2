# Generated by Django 4.2 on 2023-05-28 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0002_remove_mail_id_alter_mail_threadid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='ExpiryTime',
            field=models.CharField(max_length=100),
        ),
    ]
