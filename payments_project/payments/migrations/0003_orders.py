# Generated by Django 4.1.1 on 2022-09-14 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_alter_items_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_ids', models.ManyToManyField(to='payments.items')),
            ],
        ),
    ]