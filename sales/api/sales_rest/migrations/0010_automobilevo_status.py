# Generated by Django 4.0.3 on 2022-12-08 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_rest', '0009_remove_automobilevo_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='automobilevo',
            name='status',
            field=models.CharField(choices=[('sold', 'sold'), ('available', 'available')], default='available', max_length=100),
        ),
    ]