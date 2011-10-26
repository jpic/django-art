from django.db import models
from django.utils.translation import ugettext as _

from mptt.models import MPTTModel, TreeForeignKey

class Oeuvre(models.Model):
    # object description
    inventory_number = models.IntegerField(null=True, blank=True)
    previous_inventory_number = models.IntegerField(null=True, blank=True)
    other_inventory_numbers = models.CharField(max_length=100, null=True, blank=True)
    
    domains = models.ManyToManyField('Domain', null=True, blank=True)
    
    designation = models.CharField(max_length=100)
    author = models.ForeignKey('Author', null=True, blank=True)
    author_details = models.TextField(null=True, blank=True)
    school = models.ForeignKey('School', null=True, blank=True)
    previous_attributions = models.TextField(null=True, blank=True)
    period = models.ForeignKey('Period', null=True, blank=True)
    vintage = models.CharField(max_length=100, null=True, blank=True)
    absolute_dating = models.ForeignKey('Dating', null=True, blank=True)
    absolute_dating_details = models.TextField(null=True, blank=True)
    dating_laboratory = models.CharField(max_length=100, null=True, blank=True)
    style_era = models.ForeignKey('StyleEra', null=True, blank=True)
    original_copy_period = models.ForeignKey('Period', null=True, blank=True, 
        related_name='original_period_of_oeuvres')
    material_techniques = models.TextField(null=True, blank=True)
    dimensions = models.CharField(max_length=100, null=True, blank=True)
    inscriptions = models.ManyToManyField('Inscription', null=True, blank=True)
    inscriptions_details = models.TextField(null=True, blank=True)
    onomastic = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    current_conservation_state = models.CharField(max_length=100, null=True, blank=True)
    representation = models.CharField(max_length=100, null=True, blank=True)
    representation_details = models.TextField(null=True, blank=True)
    representation_date = models.DateField(null=True, blank=True)
    representation_source = models.CharField(max_length=100, null=True, blank=True)

    # historical context
    genes = models.CharField(max_length=100, null=True, blank=True, 
        help_text=_('creation state, mention of related oeuvres'))
    history = models.TextField(null=True, blank=True, 
        help_text=_('details about genes'))
    creation_locations = models.ForeignKey('GeographicalLocation', null=True, blank=True, 
        help_text=_('location of creation, execution'))
    creation_locations_details = models.TextField(null=True, blank=True, 
        help_text=_('details about the location of creation, execution; usage'))
    geographical_history = models.TextField(null=True, blank=True)
    usage = models.CharField(max_length=100, null=True, blank=True, 
        help_text=_('usage, destination'))
    usage_details = models.TextField(null=True, blank=True,
        help_text=_('usage, destination details'))
    usage_locations = models.CharField(max_length=100, null=True, blank=True)
    usage_period = models.ForeignKey('Period', null=True, blank=True,
        related_name='used_oeuvres')
    usage_vintage = models.CharField(max_length=100, null=True, blank=True)
    origin = models.CharField(max_length=100, null=True, blank=True,
        help_text=_('discovery, origin, collect'))
    origin_details = models.TextField(null=True, blank=True)
    sda_site_number = models.IntegerField(null=True, blank=True)
    
    # legal
    legal_state = models.ForeignKey('LegalState', null=True, blank=True)
    acquisition_date = models.DateField(null=True, blank=True)
    previous_belonging = models.CharField(max_length=100, null=True, blank=True)
    previous_depots = models.TextField(null=True, blank=True)
    depot = models.CharField(max_length=100, null=True, blank=True)
    depot_date = models.DateField(null=True, blank=True)
    preservation_location = models.TextField(null=True, blank=True)
    acquisition_intermediary = models.TextField(null=True, blank=True)
    
    # more info
    bibliography = models.TextField(null=True, blank=True)
    exposure = models.TextField(null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    photograph = models.TextField(null=True, blank=True)
    editor = models.TextField(null=True, blank=True)
    copyright = models.TextField(null=True, blank=True)
    
    # medias
    image = models.ImageField(upload_to='oeuvre_image', null=True, blank=True)
    video = models.URLField(null=True, blank=True)
    audio = models.FileField(upload_to='ouvre_audio', null=True, blank=True)
    
    # accounting
    estimation = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    purchase_price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    sale_price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)

    # landings
    landed_by = models.CharField(max_length=100, null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return self.designation
    
    class Meta:
        ordering = ('designation',)

class Dating(MPTTModel):
    name = models.CharField(max_length=100, null=True, blank=True)
    parent = TreeForeignKey('Dating', null=True, blank=True, related_name='children')

    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)

class GeographicalLocation(MPTTModel):
    name = models.CharField(max_length=200, null=True, blank=True)
    parent = TreeForeignKey('GeographicalLocation', null=True, blank=True, related_name='children')

    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)

class Inscription(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)

class School(MPTTModel):
    name = models.CharField(max_length=100, null=True, blank=True)
    parent = TreeForeignKey('School', null=True, blank=True, related_name='children')

    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)

class StyleEra(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)

class Domain(MPTTModel):
    name = models.CharField(max_length=100, null=True, blank=True)
    parent = TreeForeignKey('Domain', null=True, blank=True, related_name='children')

    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)

class Author(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    aliases = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)

class LegalState(MPTTModel):
    name = models.CharField(max_length=100, null=True, blank=True)
    parent = TreeForeignKey('LegalState', null=True, blank=True, related_name='children')

    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)

class Period(MPTTModel):
    name = models.CharField(max_length=100, null=True, blank=True)
    parent = TreeForeignKey('Period', null=True, blank=True, related_name='children')

    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)
