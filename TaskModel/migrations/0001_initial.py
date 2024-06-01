# Generated by Django 5.0.6 on 2024-06-01 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('TaskTitle', models.CharField(max_length=50)),
                ('TaskDescription', models.TextField()),
                ('isCompleted', models.BooleanField(default=False)),
                ('TaskAssignDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
