# Generated by Django 3.2.6 on 2021-11-22 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0002_material_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='produtos'),
        ),
    ]
