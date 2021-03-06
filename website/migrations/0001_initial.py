# Generated by Django 3.2.12 on 2022-02-25 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(choices=[('EAST', 'East'), ('WEST', 'West'), ('NORTH', 'North'), ('SOUTH', 'South')], default='EAST', max_length=50)),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShopName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('addr', models.CharField(blank=True, max_length=250, null=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.areaname')),
            ],
        ),
        migrations.CreateModel(
            name='Furniture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=150, null=True)),
                ('description', models.TextField()),
                ('status', models.BooleanField(blank=True, default=True, null=True)),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.shopname')),
            ],
        ),
    ]
