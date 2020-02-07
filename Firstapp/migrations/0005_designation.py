# Generated by Django 2.2.4 on 2020-02-06 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Firstapp', '0004_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='designation',
            fields=[
                ('designation_id', models.AutoField(primary_key=True, serialize=False)),
                ('designation_name', models.CharField(max_length=255)),
                ('added_by', models.CharField(default='', max_length=255)),
                ('edited_by', models.CharField(default='', max_length=255)),
                ('deleted_by', models.CharField(default='', max_length=255)),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Firstapp.department')),
            ],
        ),
    ]
