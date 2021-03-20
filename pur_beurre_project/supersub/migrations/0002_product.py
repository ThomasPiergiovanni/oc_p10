# Generated by Django 3.1.7 on 2021-03-20 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supersub', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_origin', models.CharField(max_length=200)),
                ('product_name', models.CharField(max_length=200)),
                ('nutriscore_grade', models.CharField(max_length=8)),
                ('fatty_acids', models.DecimalField(decimal_places=3, max_digits=8)),
                ('saturated_fatty_acids', models.DecimalField(decimal_places=3, max_digits=8)),
                ('sugar', models.DecimalField(decimal_places=3, max_digits=8)),
                ('salt', models.DecimalField(decimal_places=3, max_digits=8)),
                ('image', models.URLField()),
                ('url', models.URLField()),
            ],
        ),
    ]
