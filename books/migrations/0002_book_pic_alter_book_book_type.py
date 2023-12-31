# Generated by Django 4.2.1 on 2023-06-15 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pic',
            field=models.ImageField(default='fart-cat.jpg', upload_to='books'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_type',
            field=models.CharField(choices=[('hardcover', 'Hard cover'), ('ebook', 'E-Book'), ('audiob', 'Audiobook')], default='hardcover', max_length=12),
        ),
    ]
