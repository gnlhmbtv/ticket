# Generated by Django 3.2.8 on 2023-12-20 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_product_form_factor'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.ManyToManyField(blank=True, db_index=True, null=True, related_name='color_product', to='core.Color', verbose_name='Color'),
        ),
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.IntegerField(blank=True, default=1959, verbose_name='Rating'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
    ]
