# Generated by Django 3.2.5 on 2021-08-29 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dich',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('some1', models.SmallIntegerField()),
                ('some2', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Dich2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('some_types', models.IntegerField(choices=[(1, 'тип 1'), (2, 'тип 2')])),
                ('key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fair.dich')),
            ],
        ),
    ]