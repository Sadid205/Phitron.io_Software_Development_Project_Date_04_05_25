# Generated by Django 5.0.6 on 2024-06-07 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('PhoneNumber', models.IntegerField(max_length=11)),
                ('InstrumentType', models.CharField(max_length=50)),
            ],
        ),
    ]