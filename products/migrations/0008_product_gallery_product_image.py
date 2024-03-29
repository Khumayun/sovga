# Generated by Django 2.0.7 on 2019-04-10 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20190403_1226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Title')),
            ],
            options={
                'verbose_name_plural': 'Galleries',
            },
        ),
        migrations.CreateModel(
            name='Product_image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='photos/%Y/%m/%d/', verbose_name='File')),
                ('gallery', models.ForeignKey(blank=True, null=True, on_delete=True, related_name='images', to='products.Product_gallery')),
            ],
        ),
    ]
