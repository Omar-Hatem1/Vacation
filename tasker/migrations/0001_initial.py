# Generated by Django 4.1.7 on 2023-03-14 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('description', models.CharField(blank=True, max_length=150, null=True)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='tasker/files/tasks')),
                ('status', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('receivers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receivers', to='tasker.staff')),
                ('staff', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tasker.staff')),
            ],
        ),
        migrations.CreateModel(
            name='TaskResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('description', models.CharField(blank=True, max_length=150, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='tasker/files/responses')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tasker.task')),
            ],
        ),
    ]