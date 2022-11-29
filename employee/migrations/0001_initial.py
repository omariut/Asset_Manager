# Generated by Django 4.1.3 on 2022-11-29 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('employee_id', models.CharField(max_length=50)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='company.company')),
            ],
            options={
                'db_table': 'employees',
                'ordering': ['-created_at'],
            },
        ),
    ]