# Generated by Django 2.0.7 on 2018-07-08 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180708_0527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='registrations', to='accounts.Student'),
        ),
    ]
