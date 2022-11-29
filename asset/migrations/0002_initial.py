# Generated by Django 4.1.3 on 2022-11-29 13:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('asset', '0001_initial'),
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='handoverorreturn',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='admin', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='handoverorreturn',
            name='asset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='asset.asset'),
        ),
        migrations.AddField(
            model_name='handoverorreturn',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='handoverorreturn',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='employee.employee'),
        ),
        migrations.AddField(
            model_name='handoverorreturn',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='category',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='company.company'),
        ),
        migrations.AddField(
            model_name='category',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='category',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='asset',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='asset.category'),
        ),
        migrations.AddField(
            model_name='asset',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='asset',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddIndex(
            model_name='handoverorreturn',
            index=models.Index(fields=['-created_at'], name='handovers_created_8bab83_idx'),
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['-created_at'], name='categories_created_9211a1_idx'),
        ),
        migrations.AddIndex(
            model_name='asset',
            index=models.Index(fields=['-created_at'], name='assets_created_d09603_idx'),
        ),
    ]