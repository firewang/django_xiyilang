# Generated by Django 2.0.1 on 2018-03-05 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('novel', '0002_auto_20180305_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='b',
            field=models.ForeignKey(default='999', on_delete=django.db.models.deletion.DO_NOTHING, to='novel.Bussiness'),
        ),
    ]