# Generated by Django 3.2.7 on 2021-09-14 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=256)),
                ('telefone', models.CharField(max_length=20)),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoa.pessoa')),
            ],
        ),
    ]
