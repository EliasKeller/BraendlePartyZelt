# Generated by Django 2.1.5 on 2019-03-11 13:36

from django.db import migrations, models
import django_enumfield.db.fields
import tent.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', django_enumfield.db.fields.EnumField(default=0, enum=tent.models.TentType)),
                ('width', models.IntegerField()),
                ('length', models.IntegerField()),
                ('number_of_People', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]