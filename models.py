# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Basicinfo(models.Model):
    id = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    validity = models.TextField(blank=True, null=True)
    blank_pages = models.TextField(blank=True, null=True)
    vaccination = models.TextField(blank=True, null=True)
    amount_entry = models.TextField(blank=True, null=True)
    amount_exit = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'basicinfo'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MysiteBasicinfo(models.Model):
    country = models.CharField(db_column='Country', unique=True, max_length=200)  # Field name made lowercase.
    passport_validity = models.CharField(db_column='Passport_Validity', max_length=300)  # Field name made lowercase.
    blank_passport_pages = models.CharField(db_column='Blank_Passport_pages', max_length=300)  # Field name made lowercase.
    tourist_visa_required = models.CharField(db_column='Tourist_visa_required', max_length=300)  # Field name made lowercase.
    vacction = models.CharField(db_column='Vacction', max_length=300)  # Field name made lowercase.
    currency_restriction_for_entry = models.CharField(db_column='Currency_restriction_For_Entry', max_length=300)  # Field name made lowercase.
    currency_restriction_for_exit = models.CharField(db_column='Currency_restriction_For_Exit', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mysite_basicinfo'


class MysiteQuickFacts(models.Model):
    country = models.CharField(db_column='Country', unique=True, max_length=200)  # Field name made lowercase.
    passport_validity = models.CharField(db_column='Passport_Validity', max_length=300)  # Field name made lowercase.
    vacction = models.CharField(db_column='Vacction', max_length=300)  # Field name made lowercase.
    blank_passport_pages = models.CharField(db_column='Blank_Passport_pages', max_length=300)  # Field name made lowercase.
    currency_restriction_for_entry = models.CharField(db_column='Currency_restriction_For_Entry', max_length=300)  # Field name made lowercase.
    tourist_visa_required = models.CharField(db_column='Tourist_visa_required', max_length=300)  # Field name made lowercase.
    currency_restriction_for_exit = models.CharField(db_column='Currency_restriction_For_Exit', max_length=300)  # Field name made lowercase.
    country_photo = models.CharField(db_column='Country_photo', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mysite_quick_facts'


class MysiteScholars(models.Model):
    country = models.CharField(db_column='Country', max_length=100)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=5000)  # Field name made lowercase.
    level = models.CharField(max_length=15)
    last_date = models.DateField()
    scholarship = models.CharField(max_length=20)
    eligibility = models.CharField(db_column='Eligibility', max_length=5000)  # Field name made lowercase.
    benefits = models.CharField(db_column='Benefits', max_length=5000)  # Field name made lowercase.
    application = models.CharField(db_column='Application', max_length=5000)  # Field name made lowercase.
    link = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'mysite_scholars'


class MysiteTourism(models.Model):
    country = models.CharField(db_column='Country', unique=True, max_length=200)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=5000)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mysite_tourism'


class VisaInformation(models.Model):
    name = models.TextField(blank=True, null=True)
    study_visa = models.TextField(blank=True, null=True)
    visit_visa = models.TextField(blank=True, null=True)
    business_visa = models.TextField(blank=True, null=True)
    employment_visa = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'visa_information'
