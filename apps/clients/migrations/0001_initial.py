# Generated by Django 4.0 on 2022-03-10 03:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('resellers', '0001_initial'),
        ('core', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.IntegerField(default=117100)),
            ],
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.IntegerField(unique=True)),
                ('ip_username', models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='IP/Username')),
                ('address', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=100)),
                ('paid', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('olt_details', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.olt')),
                ('onu_details', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.onu')),
                ('package_details', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.package')),
                ('pop_details', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.pop')),
                ('reseller', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='resellers.resellers')),
                ('router_details', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.router')),
                ('switch_details', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.switch')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]
