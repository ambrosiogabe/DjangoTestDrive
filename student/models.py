from django.db import models

# Create your models here.
class Student(models.Model):
    s_id = models.AutoField(db_column='S_ID', primary_key=True)  # Field name made lowercase.
    s_last = models.CharField(db_column='S_Last', max_length=255)  # Field name made lowercase.
    s_first = models.CharField(db_column='S_First', max_length=255)  # Field name made lowercase.
    s_mi = models.CharField(db_column='S_Mi', max_length=255)  # Field name made lowercase.
    s_address = models.CharField(db_column='S_Address', max_length=255)  # Field name made lowercase.
    s_city = models.CharField(db_column='S_City', max_length=100)  # Field name made lowercase.
    s_state = models.CharField(db_column='S_State', max_length=100)  # Field name made lowercase.
    s_zip = models.CharField(db_column='S_Zip', max_length=100)  # Field name made lowercase.
    s_phone = models.CharField(db_column='S_Phone', max_length=100)  # Field name made lowercase.
    s_class = models.CharField(db_column='S_Class', max_length=100)  # Field name made lowercase.
    f_id = models.CharField(db_column='F_ID', max_length=100)  # Field name made lowercase.
    s_pin = models.CharField(db_column='S_Pin', max_length=100)  # Field name made lowercase.
    s_dob = models.DateTimeField(db_column='S_Dob')  # Field name made lowercase.
    date_enrolled = models.CharField(db_column='Date_Enrolled', max_length=100)  # Field name made lowercase.
