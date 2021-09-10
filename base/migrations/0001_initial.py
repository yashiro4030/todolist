# Generated by Django 3.2.7 on 2021-09-09 11:29

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
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('systeme', models.CharField(blank=True, max_length=50, null=True)),
                ('service', models.CharField(blank=True, max_length=50, null=True)),
                ('check', models.BooleanField(default=False)),
                ('create', models.DateTimeField(auto_now=True)),
                ('action', models.TextField(blank=True, max_length=200, null=True)),
                ('remarque', models.TextField(blank=True, max_length=200, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['check'],
            },
        ),
    ]
