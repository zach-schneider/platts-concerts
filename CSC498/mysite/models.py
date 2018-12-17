from django.db import models


class Events(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField(db_column='YEAR', blank=True, null=True)  # Field name made lowercase.
    day = models.TextField(db_column='DAY', blank=True, null=True)  # Field name made lowercase.
    date = models.TextField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    time = models.TextField(db_column='TIME', blank=True, null=True)  # Field name made lowercase.
    artist = models.TextField(db_column='ARTIST', blank=True, null=True)  # Field name made lowercase.
    appearing_with = models.TextField(db_column='APPEARING_WITH', blank=True, null=True)  # Field name made lowercase.
    venue = models.TextField(db_column='VENUE', blank=True, null=True)  # Field name made lowercase.
    price_student = models.TextField(db_column='PRICE_Student', blank=True, null=True)  # Field name made lowercase.
    price_public = models.TextField(db_column='PRICE_public', blank=True, null=True)  # Field name made lowercase.
    cp_nl_ad = models.TextField(db_column='CP_NL_AD', blank=True, null=True)  # Field name made lowercase.
    page = models.TextField(db_column='PAGE', blank=True, null=True)  # Field name made lowercase.
    cp_rev = models.TextField(db_column='CP_REV', blank=True, null=True)  # Field name made lowercase.
    page_1 = models.TextField(db_column='PAGE_1', blank=True, null=True)  # Field name made lowercase.
    cp_preview = models.TextField(db_column='CP_PREVIEW', blank=True, null=True)  # Field name made lowercase.
    page_2 = models.TextField(db_column='PAGE_2', blank=True, null=True)  # Field name made lowercase.
    cp_letters_1 = models.TextField(db_column='CP_LETTERS_1', blank=True, null=True)  # Field name made lowercase.
    page_3 = models.TextField(db_column='PAGE_3', blank=True, null=True)  # Field name made lowercase.
    cp_letters_2 = models.TextField(db_column='CP_LETTERS_2', blank=True, null=True)  # Field name made lowercase.
    page_4 = models.TextField(db_column='PAGE_4', blank=True, null=True)  # Field name made lowercase.
    cp_letters_3 = models.TextField(db_column='CP_LETTERS_3', blank=True, null=True)  # Field name made lowercase.
    page_5 = models.TextField(db_column='PAGE_5', blank=True, null=True)  # Field name made lowercase.
    cp_eds = models.TextField(db_column='CP_EDS', blank=True, null=True)  # Field name made lowercase.
    page_6 = models.TextField(db_column='PAGE_6', blank=True, null=True)  # Field name made lowercase.
    yrbk = models.TextField(db_column='YRBK', blank=True, null=True)  # Field name made lowercase.
    page_7 = models.TextField(db_column='PAGE_7', blank=True, null=True)  # Field name made lowercase.
    pr_article = models.TextField(db_column='PR_ARTICLE', blank=True, null=True)  # Field name made lowercase.
    pr_page = models.TextField(db_column='PR_PAGE', blank=True, null=True)  # Field name made lowercase.
    beekman_st = models.TextField(db_column='BEEKMAN_ST', blank=True, null=True)  # Field name made lowercase.
    beek_st_pg = models.TextField(db_column='BEEK_ST_PG', blank=True, null=True)  # Field name made lowercase.
    weekly = models.TextField(db_column='WEEKLY', blank=True, null=True)  # Field name made lowercase.
    wkly_pg = models.TextField(db_column='WKLY_PG', blank=True, null=True)  # Field name made lowercase.
    verification = models.TextField(db_column='VERIFICATION', blank=True, null=True)  # Field name made lowercase.
    sa_box = models.TextField(db_column='SA_BOX', blank=True, null=True)  # Field name made lowercase.
    file = models.TextField(db_column='FILE', blank=True, null=True)  # Field name made lowercase.
    flat_fee = models.TextField(db_column='FLAT_FEE', blank=True, null=True)  # Field name made lowercase.
    light_sound = models.TextField(db_column='LIGHT_SOUND', blank=True, null=True)  # Field name made lowercase.
    percentage = models.TextField(db_column='PERCENTAGE', blank=True, null=True)  # Field name made lowercase.
    other_fee = models.TextField(db_column='OTHER_FEE', blank=True, null=True)  # Field name made lowercase.
    total_cost = models.TextField(db_column='TOTAL_COST', blank=True, null=True)  # Field name made lowercase.
    speaker = models.TextField(db_column='SPEAKER', blank=True, null=True)  # Field name made lowercase.
    notes_1 = models.TextField(db_column='NOTES_1', blank=True, null=True)  # Field name made lowercase.
    notes_2 = models.TextField(db_column='NOTES_2', blank=True, null=True)  # Field name made lowercase.
    notes_3 = models.TextField(db_column='NOTES_3', blank=True, null=True)  # Field name made lowercase.
    notes_4 = models.TextField(db_column='NOTES_4', blank=True, null=True)  # Field name made lowercase.
    notes_5 = models.TextField(db_column='NOTES_5', blank=True, null=True)  # Field name made lowercase.
    column45 = models.TextField(db_column='Column45', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EVENTS'


class FieldTags(models.Model):
    column = models.TextField(db_column='COLUMN', blank=True, null=True)  # Field name made lowercase.
    field_tag = models.TextField(db_column='FIELD_TAG', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FIELD TAGS'


class Sheet3(models.Model):
    year = models.IntegerField(db_column='YEAR', blank=True, null=True)  # Field name made lowercase.
    sa_budget = models.TextField(db_column='SA_BUDGET', blank=True, null=True)  # Field name made lowercase.
    acb_budget = models.TextField(db_column='ACB_BUDGET', blank=True, null=True)  # Field name made lowercase.
    concert_budget = models.TextField(db_column='CONCERT_BUDGET', blank=True, null=True)  # Field name made lowercase.
    sa_fee = models.TextField(db_column='SA_FEE', blank=True, null=True)  # Field name made lowercase.
    students = models.TextField(db_column='STUDENTS', blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='NOTES', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sheet3'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
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
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
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
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
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
