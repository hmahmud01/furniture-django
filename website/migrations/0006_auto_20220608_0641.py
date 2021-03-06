# Generated by Django 3.2.12 on 2022-06-08 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='description',
            new_name='msg',
        ),
        migrations.AddField(
            model_name='order',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
