# Generated by Django 4.2 on 2023-05-10 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0016_pump_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pump',
            name='Privacy',
        ),
        migrations.RemoveField(
            model_name='pump',
            name='budget',
        ),
        migrations.RemoveField(
            model_name='pump',
            name='phone',
        ),
        migrations.AddField(
            model_name='pump',
            name='kun_mal',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pump',
            name='oy_mal',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pump',
            name='soat_mal',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pump',
            name='yil_mal',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
