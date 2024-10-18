# Generated by Django 5.1.2 on 2024-10-18 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('CPU', 'Processors'), ('GPU', 'Graphic Cards'), ('KEYMOU', 'Keyboards & Mouses'), ('PC', 'Gaming PCs'), ('OTHER', 'Others')], default='OTHER', max_length=6),
        ),
    ]