# Generated by Django 3.0.3 on 2020-03-28 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='competition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('date', models.DateField()),
                ('competitor_one', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='competitor_one', to='user.student')),
                ('competitor_two', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='competitor_two', to='user.student')),
            ],
        ),
    ]
