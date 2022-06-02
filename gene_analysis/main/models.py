from django.db import models


class Genes(models.Model):
    index = models.BigIntegerField(primary_key=True)
    unnamed_0 = models.BigIntegerField(db_column='Unnamed: 0', blank=True, null=True)
    x = models.BigIntegerField(db_column='X', blank=True, null=True)
    original_request = models.TextField(db_column='Original_request', blank=True, null=True)
    function = models.TextField(db_column='Function', blank=True, null=True)
    entry = models.TextField(db_column='Entry', blank=True, null=True)
    entry_name = models.TextField(db_column='Entry_name', blank=True, null=True)
    protein_names = models.TextField(db_column='Protein_names', blank=True, null=True)
    gene_names = models.TextField(db_column='Gene_names', blank=True, null=True)
    organism = models.TextField(db_column='Organism', blank=True, null=True)
    length = models.BigIntegerField(db_column='Length', blank=True, null=True)
    go = models.TextField(db_column='GO', blank=True, null=True)
    disease = models.TextField(db_column='Disease', blank=True, null=True)
    expr = models.TextField(db_column='Expr', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genes'


'''
class FavoriteGroup(models.Model):
    group_id = models.BigIntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'favorite_group'


class Favorite(models.Model):
    favorite_id = models.ForeignKey(FavoriteGroup, on_delete=models.CASCADE)
    xcoord = models.FloatField(blank=False, null=False)
    ycoord = models.FloatField(blank=False, null=False)
    label = models.IntegerField(blank=False, null=False)
    gene_id = models.ForeignKey(Genes, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'favorite'
'''
