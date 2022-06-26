# Generated by Django 4.0.4 on 2022-06-23 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_options_alter_autor_fecha_creacion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254)),
                ('tipo_contacto', models.IntegerField(choices=[[0, 'Consulta'], [1, 'Reclamo'], [2, 'Segurencia'], [3, 'Feliciaciones']])),
                ('mensaje', models.TextField()),
                ('avisos', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
