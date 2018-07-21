# Generated by Django 2.0 on 2018-04-14 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('s_id', models.AutoField(db_column='S_ID', primary_key=True, serialize=False)),
                ('s_last', models.CharField(blank=True, db_column='S_Last', max_length=255, null=True)),
                ('s_first', models.CharField(blank=True, db_column='S_First', max_length=255, null=True)),
                ('s_mi', models.CharField(blank=True, db_column='S_Mi', max_length=255, null=True)),
                ('s_address', models.CharField(blank=True, db_column='S_Address', max_length=255, null=True)),
                ('s_city', models.CharField(blank=True, db_column='S_City', max_length=100, null=True)),
                ('s_state', models.CharField(blank=True, db_column='S_State', max_length=100, null=True)),
                ('s_zip', models.CharField(blank=True, db_column='S_Zip', max_length=100, null=True)),
                ('s_phone', models.CharField(blank=True, db_column='S_Phone', max_length=100, null=True)),
                ('s_class', models.CharField(blank=True, db_column='S_Class', max_length=100, null=True)),
                ('f_id', models.CharField(blank=True, db_column='F_ID', max_length=100, null=True)),
                ('s_pin', models.CharField(blank=True, db_column='S_Pin', max_length=100, null=True)),
                ('s_dob', models.DateTimeField(blank=True, db_column='S_Dob', null=True)),
                ('date_enrolled', models.CharField(blank=True, db_column='Date_Enrolled', max_length=100, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'STUDENT',
            },
        ),
    ]
