# Generated by Django 3.2.9 on 2021-11-10 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atracao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=1500)),
                ('descricao', models.TextField()),
                ('horario_func', models.TextField()),
                ('idade_minima', models.IntegerField()),
            ],
        ),
    ]
