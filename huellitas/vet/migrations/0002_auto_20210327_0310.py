# Generated by Django 3.1.7 on 2021-03-27 03:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=10)),
                ('address', models.TextField(max_length=1000)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('phone', models.CharField(max_length=20, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='petdate',
            name='office',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='offices', to='vet.office'),
        ),
    ]