# Generated by Django 4.0.4 on 2022-05-02 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0002_item_item_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_imagem',
            field=models.CharField(default='https://cdn-icons-png.flaticon.com/512/459/459122.png ', max_length=800),
        ),
    ]
