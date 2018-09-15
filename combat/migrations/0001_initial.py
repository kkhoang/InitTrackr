# Generated by Django 2.1.1 on 2018-09-12 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('perception', models.IntegerField(default=10)),
                ('armorclass', models.IntegerField(default=10)),
                ('hitpoints', models.IntegerField(default=30)),
                ('initiative', models.IntegerField(default=0)),
            ],
        ),
    ]