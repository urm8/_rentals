# Generated by Django 4.0.4 on 2022-04-13 18:05

from django.db import migrations
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservation',
            options={'ordering': ('rental', django.db.models.expressions.OrderBy(django.db.models.expressions.F('checkin'), descending=True, nulls_first=True))},
        ),
    ]