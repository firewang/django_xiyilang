# Generated by Django 2.0.1 on 2018-03-05 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novel', '0004_auto_20180305_1435'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='aaa', max_length=32, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='bussiness',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
