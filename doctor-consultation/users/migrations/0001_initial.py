# Generated by Django 4.0.2 on 2022-02-20 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authn', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='patientDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientName', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(blank=True, max_length=7, null=True)),
                ('contactNumber', models.IntegerField()),
                ('bloodGroup', models.CharField(blank=True, max_length=5, null=True)),
                ('date', models.CharField(max_length=11)),
                ('status', models.CharField(blank=True, max_length=15, null=True)),
                ('problem', models.CharField(blank=True, max_length=200, null=True)),
                ('tabletsDetails', models.CharField(blank=True, max_length=200, null=True)),
                ('userdet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authn.userdetails')),
            ],
        ),
    ]
