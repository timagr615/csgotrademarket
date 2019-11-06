# Generated by Django 2.2.6 on 2019-11-06 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_bot_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weapon',
            old_name='market_mame',
            new_name='market_name',
        ),
        migrations.RenameField(
            model_name='weapon',
            old_name='descriptions',
            new_name='tradable_after',
        ),
        migrations.RemoveField(
            model_name='weapon',
            name='owner_descriptions',
        ),
        migrations.RemoveField(
            model_name='weapon',
            name='tags',
        ),
        migrations.AlterField(
            model_name='weapon',
            name='bot',
            field=models.ForeignKey(db_column='login', null=True, on_delete=django.db.models.deletion.CASCADE, to='market.Bot'),
        ),
    ]
