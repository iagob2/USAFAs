# Generated by Django 5.1.2 on 2024-11-28 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protoDigital', '0003_alter_usuario_senha'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usafa',
            old_name='endereco_usafa_cidade',
            new_name='telefone_usafa',
        ),
        migrations.RemoveField(
            model_name='usafa',
            name='endereco_usafa_estado',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='CEP',
            field=models.CharField(max_length=9),
        ),
    ]