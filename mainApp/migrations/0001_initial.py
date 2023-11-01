# Generated by Django 4.2.6 on 2023-11-01 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('logo', models.FileField(upload_to='')),
                ('davlat', models.CharField(max_length=255)),
                ('prezident', models.CharField(blank=True, max_length=255)),
                ('murabbiy', models.CharField(blank=True, max_length=255)),
                ('yili', models.DateField(blank=True)),
                ('record_trans', models.DateField(blank=True, max_length=255)),
                ('record_sotuv', models.DateField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=255)),
                ('davlat', models.CharField(max_length=255)),
                ('narx', models.FloatField()),
                ('t_sana', models.DateField()),
                ('pozitsiya', models.CharField(max_length=255)),
                ('club', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainApp.club')),
            ],
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('narx', models.FloatField()),
                ('tax_narx', models.FloatField()),
                ('mavsum', models.CharField(max_length=255)),
                ('eski_club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sotuvlari', to='mainApp.club')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.player')),
                ('yangi_club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.club')),
            ],
        ),
    ]