# Generated by Django 4.2 on 2023-05-17 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasker', '0005_leaverequest_sender_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaverequest',
            name='sender_role',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]