from django.db import models


class UserRole(models.Model):
    user = models.ForeignKey('UserTable', models.DO_NOTHING)
    roles = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_role'


class UserTable(models.Model):
    id = models.BigIntegerField(primary_key=True)
    active = models.BooleanField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_table'


class Genes(models.Model):
    index = models.BigIntegerField(primary_key=True)
    unnamed_0 = models.BigIntegerField(db_column='Unnamed: 0', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    x = models.BigIntegerField(db_column='X', blank=True, null=True)  # Field name made lowercase.
    original_request = models.TextField(db_column='Original_request', blank=True, null=True)  # Field name made lowercase.
    function = models.TextField(db_column='Function', blank=True, null=True)  # Field name made lowercase.
    entry = models.TextField(db_column='Entry', blank=True, null=True)  # Field name made lowercase.
    entry_name = models.TextField(db_column='Entry_name', blank=True, null=True)  # Field name made lowercase.
    protein_names = models.TextField(db_column='Protein_names', blank=True, null=True)  # Field name made lowercase.
    gene_names = models.TextField(db_column='Gene_names', blank=True, null=True)  # Field name made lowercase.
    organism = models.TextField(db_column='Organism', blank=True, null=True)  # Field name made lowercase.
    length = models.BigIntegerField(db_column='Length', blank=True, null=True)  # Field name made lowercase.
    go = models.TextField(db_column='GO', blank=True, null=True)  # Field name made lowercase.
    disease = models.TextField(db_column='Disease', blank=True, null=True)  # Field name made lowercase.
    expr = models.TextField(db_column='Expr', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genes'
