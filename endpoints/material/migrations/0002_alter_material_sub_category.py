# Generated by Django 5.0.6 on 2024-12-16 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='sub_category',
            field=models.CharField(choices=[('Sheet Metal', 'Sheet Metal'), ('Cast Iron', 'Cast Iron'), ('Hardwood', 'Hardwood'), ('Plywood', 'Plywood'), ('Reinforced Concrete', 'Reinforced Concrete'), ('Thermoplastic', 'Thermoplastic'), ('Tempered Glass', 'Tempered Glass'), ('Steel', 'Steel'), ('Aluminum', 'Aluminum'), ('Softwood', 'Softwood'), ('Laminated Glass', 'Laminated Glass'), ('Frosted Glass', 'Frosted Glass')], default='Sheet Metal', max_length=50),
        ),
    ]
