# Generated by Django 3.2.16 on 2023-03-06 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0004_alter_aluno_data_nascimento'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='nome',
            field=models.CharField(default=' ', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aluno',
            name='rg',
            field=models.CharField(default=' ', max_length=9),
            preserve_default=False,
        ),
    ]
