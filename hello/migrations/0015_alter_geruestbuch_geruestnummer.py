# Generated by Django 5.0.2 on 2024-02-25 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0014_alter_geruestbuch_grund'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geruestbuch',
            name='Geruestnummer',
            field=models.AutoField(help_text='Die Gerüstnummer wird automatisch erzeugt.', primary_key=True, serialize=False),
        ),
    ]
