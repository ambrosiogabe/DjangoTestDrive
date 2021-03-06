# Generated by Django 2.0 on 2018-04-14 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20180414_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date_enrolled',
            field=models.CharField(db_column='Date_Enrolled', max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='f_id',
            field=models.CharField(db_column='F_ID', max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='s_address',
            field=models.CharField(db_column='S_Address', max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='s_city',
            field=models.CharField(db_column='S_City', max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='s_class',
            field=models.CharField(db_column='S_Class', max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='s_dob',
            field=models.DateTimeField(db_column='S_Dob'),
        ),
        migrations.AlterField(
            model_name='student',
            name='s_first',
            field=models.CharField(db_column='S_First', max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='s_last',
            field=models.CharField(db_column='S_Last', max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='s_mi',
            field=models.CharField(db_column='S_Mi', max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='s_phone',
            field=models.CharField(db_column='S_Phone', max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='s_pin',
            field=models.CharField(db_column='S_Pin', max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='s_state',
            field=models.CharField(db_column='S_State', max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='s_zip',
            field=models.CharField(db_column='S_Zip', max_length=100),
        ),
    ]
