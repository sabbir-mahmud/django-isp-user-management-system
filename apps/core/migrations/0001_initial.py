# Generated by Django 4.0 on 2022-03-19 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fiber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=200)),
                ('code', models.IntegerField(unique=True)),
                ('metre', models.IntegerField()),
                ('price', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Stored', 'Stored'), ('Damaged', 'Damaged')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Isp_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Mikrotik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=200)),
                ('serial_number', models.CharField(max_length=200)),
                ('pop_name', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Stored', 'Stored'), ('Damaged', 'Damaged')], default='Active', max_length=100)),
                ('price', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Olt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('serial_number', models.CharField(max_length=200, unique=True)),
                ('pon_ports', models.IntegerField()),
                ('area', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Stored', 'Stored'), ('Damaged', 'Damaged')], max_length=100)),
                ('price', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Onu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('serial_number', models.CharField(max_length=200, unique=True)),
                ('pon_mac', models.CharField(max_length=200, unique=True)),
                ('ethernet_ports', models.IntegerField()),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Stored', 'Stored'), ('Damaged', 'Damaged')], max_length=100)),
                ('price', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('speed', models.IntegerField()),
                ('ggc', models.IntegerField(default=10, verbose_name='GGC')),
                ('fna', models.IntegerField(default=10, verbose_name='FNA')),
                ('public_ip', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Router',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('mac', models.CharField(max_length=200, unique=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Stored', 'Stored'), ('Damaged', 'Damaged')], max_length=100)),
                ('price', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Switch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('serial_number', models.CharField(max_length=200, unique=True)),
                ('ethernet_ports', models.IntegerField()),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Stored', 'Stored'), ('Damaged', 'Damaged')], max_length=100)),
                ('price', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pop_name', models.CharField(max_length=200)),
                ('users', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('main_pop_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.pop')),
            ],
        ),
    ]
