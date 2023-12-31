# Generated by Django 4.2.5 on 2023-09-20 08:10

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='exercice', max_length=255)),
                ('description', models.TextField(default='description')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_name', models.CharField(default='myNewSession', max_length=255)),
                ('creation_date', models.DateTimeField(default=datetime.datetime(2023, 9, 20, 8, 10, 29, 799241, tzinfo=datetime.timezone.utc))),
            ],
        ),
        migrations.CreateModel(
            name='SessionExercice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repetitions', models.PositiveIntegerField(default=20, validators=[django.core.validators.MinValueValidator(20), django.core.validators.MaxValueValidator(100)])),
                ('exercice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercices.exercice')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercices.session')),
            ],
        ),
        migrations.AddField(
            model_name='session',
            name='exercices',
            field=models.ManyToManyField(through='exercices.SessionExercice', to='exercices.exercice'),
        ),
    ]
