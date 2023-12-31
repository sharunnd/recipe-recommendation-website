# Generated by Django 4.2.4 on 2023-09-02 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_rename_text_review_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='average_rating',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=3),
        ),
        migrations.AddField(
            model_name='recipe',
            name='num_reviews',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
