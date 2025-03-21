# Generated by Django 5.1.7 on 2025-03-21 16:39

import django.db.models.deletion
import stdimage.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateTimeField(auto_now_add=True, verbose_name='Data Criação')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Data Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='ativo')),
                ('cargo', models.CharField(max_length=100, verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
            },
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateTimeField(auto_now_add=True, verbose_name='Data Criação')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Data Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='ativo')),
                ('servico', models.CharField(max_length=100, verbose_name='Serviço')),
                ('descricao', models.CharField(max_length=200, verbose_name='Descrição')),
                ('icone', models.CharField(choices=[('lni-cog', 'Roda Dentada'), ('lni-stats-up', 'Gráfico'), ('lni-users', 'Utilizadores'), ('lni-layers', 'Camadas'), ('lni-mobile', 'Telemóvel'), ('lni-rocket', 'Foguete')], max_length=12, verbose_name='Icone')),
            ],
            options={
                'verbose_name': 'Serviço',
                'verbose_name_plural': 'Serviços',
            },
        ),
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateTimeField(auto_now_add=True, verbose_name='Data Criação')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Data Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='ativo')),
                ('nome', models.CharField(max_length=100)),
                ('bio', models.TextField(max_length=200, verbose_name='Biografia')),
                ('imagem', stdimage.models.StdImageField(force_min_size=False, upload_to='equipa', variations={'Thumb': {'crop': True, 'height': 480, 'width': 480}}, verbose_name='Imagem')),
                ('facebook', models.CharField(default='#', max_length=100, verbose_name='Facebook')),
                ('twitter', models.CharField(default='#', max_length=100, verbose_name='Twitter')),
                ('instagram', models.CharField(default='#', max_length=100, verbose_name='Instagram')),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cargo', verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Colaborador',
                'verbose_name_plural': 'Colaboradores',
            },
        ),
    ]
