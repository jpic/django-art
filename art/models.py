from django.db import models
from django.utils.translation import ugettext as _
from django.db.models import signals

from orderable.models import OrderableModel
from mptt.models import MPTTModel, TreeForeignKey
from admin_hack import enable_custom_values

class Artwork(models.Model):
    inventory_number = models.CharField(max_length=100, null=True, blank=True)
    old_inventory_number = models.CharField(max_length=100, null=True, blank=True)
    other_inventory_numbers = models.CharField(max_length=100, null=True, blank=True)
    
    domains = models.ManyToManyField('Domain', null=True, blank=True)
    name = models.CharField(max_length=100)
    denomination = models.ForeignKey('Denomination', null=True, blank=True)
    artist = models.ForeignKey('Artist', null=True, blank=True)
    school = models.ForeignKey('School', null=True, blank=True)
    previous_attributions = models.TextField(null=True, blank=True)
    period = models.ForeignKey('Period', null=True, blank=True)
    vintage = models.CharField(max_length=100, null=True, blank=True)
    absolute_dating = models.CharField(max_length=100, null=True, blank=True)
    absolute_dating_details = models.TextField(null=True, blank=True)
    dating_laboratory = models.CharField(max_length=100, null=True, blank=True)
    style_era = models.ForeignKey('StyleEra', null=True, blank=True)
    original_copy_period = models.ForeignKey('Period', null=True, blank=True, 
        related_name='original_period_of_oeuvres')
    material_techniques = models.ManyToManyField('MaterialTechnique', null=True, blank=True)
    dimensions = models.CharField(max_length=100, null=True, blank=True)
    inscription_types = models.ManyToManyField('InscriptionType', null=True, blank=True)
    inscriptions_details = models.TextField(null=True, blank=True)
    onomastic = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    current_conservation_state = models.CharField(max_length=100, null=True, blank=True)
    representation_subject = models.ForeignKey('RepresentationSubject', null=True, blank=True)
    representation_details = models.TextField(null=True, blank=True)
    representation_date = models.DateField(null=True, blank=True)
    representation_source = models.ForeignKey('RepresentationSource', null=True, blank=True)

    # historical context
    creation_state = models.ForeignKey('CreationState', null=True, blank=True)
    genes = models.CharField(max_length=100, null=True, blank=True, 
        help_text=_('creation state, mention of related oeuvres'))
    history = models.TextField(null=True, blank=True, 
        help_text=_('details about genes'))
    creation_locations = models.ForeignKey('GeographicalLocation', null=True, blank=True, 
        help_text=_('location of creation, execution'))
    creation_locations_details = models.TextField(null=True, blank=True, 
        help_text=_('details about the location of creation, execution; usage'))
    geographical_history = models.TextField(null=True, blank=True)
    usage = models.ForeignKey('UsageDestination', null=True, blank=True)
    usage_details = models.TextField(null=True, blank=True,
        help_text=_('usage, destination details'))
    usage_locations = models.CharField(max_length=100, null=True, blank=True)
    usage_period = models.ForeignKey('Period', null=True, blank=True,
        related_name='used_oeuvres')
    usage_vintage = models.CharField(max_length=100, null=True, blank=True)
    origin = models.CharField(max_length=100, null=True, blank=True,
        help_text=_('discovery, origin, collect'))
    collect_method = models.ForeignKey('CollectMethod', null=True, blank=True)
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

    # site
    public = models.BooleanField(verbose_name=_(u'published on the website'))

    creation_datetime = models.DateTimeField(auto_now_add=True)
    modification_datetime = models.DateTimeField(auto_now=True)

    @property
    def first_image(self):
        try:
            return self.image_set.all()[0]
        except IndexError:
            return None

    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)

class Audio(OrderableModel):
    artwork = models.ForeignKey('Artwork')
    media = models.FileField(upload_to='artwork_audio')

class Image(OrderableModel):
    artwork = models.ForeignKey('Artwork')
    media = models.ImageField(upload_to='artwork_image')

class Video(OrderableModel):
    artwork = models.ForeignKey('Artwork')
    media_url = models.URLField(null=True, blank=True)

class Artist(models.Model):
    last_name = models.CharField(max_length=250, null=True, blank=True)
    first_name = models.CharField(max_length=250, null=True, blank=True)
    name = models.CharField(max_length=250, null=True, blank=True, 
        verbose_name='artist name')
    group = models.CharField(max_length=250, null=True, blank=True)
    entitled = models.CharField(max_length=250, null=True, blank=True)
    
    nationality = models.ForeignKey('cities.Country', null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True, 
        help_text=_(u'Please enter date as YEAR-MM-DD (ie. 1872-09-26)'))
    birth_city = models.ForeignKey('cities.City', null=True, blank=True,
        related_name='born_artist_set')
    death_date = models.DateField(null=True, blank=True,
        help_text=_(u'Please enter date as YEAR-MM-DD (ie. 1894-05-21)'))
    death_city = models.ForeignKey('cities.City', null=True, blank=True,
        related_name='dead_artist_set')

    biography = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='artwork_artist',
        verbose_name=_('photo'))
   
    style_era = models.ForeignKey('StyleEra', null=True, blank=True)
    domain = models.ForeignKey('Domain', null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    
    public = models.BooleanField(verbose_name=_(u'published on the website'))
    creation_datetime = models.DateTimeField(auto_now_add=True)
    modification_datetime = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)

class NamedTreeModel(MPTTModel):
    name = models.CharField(max_length=250, null=True, blank=True)

    def __unicode__(self):
        return self.name or self.name_fr
    
    class Meta:
        ordering = ('name',)
        abstract = True

class CollectMethod(NamedTreeModel):
    parent = TreeForeignKey('CollectMethod', null=True, blank=True, 
        related_name='children')

class CreationState(NamedTreeModel):
    parent = TreeForeignKey('CreationState', null=True, blank=True, 
        related_name='children')

class Denomination(NamedTreeModel):
    parent = TreeForeignKey('Denomination', null=True, blank=True, 
        related_name='children')

class Domain(NamedTreeModel):
    parent = TreeForeignKey('Domain', null=True, blank=True, 
        related_name='children')

class InscriptionType(NamedTreeModel):
    parent = TreeForeignKey('InscriptionType', null=True, blank=True, 
        related_name='children')

class GeographicalLocation(NamedTreeModel):
    parent = TreeForeignKey('GeographicalLocation', null=True, blank=True, 
        related_name='children')

class LegalState(NamedTreeModel):
    parent = TreeForeignKey('LegalState', null=True, blank=True, 
        related_name='children')

class MaterialTechnique(NamedTreeModel):
    parent = TreeForeignKey('MaterialTechnique', null=True, blank=True, 
        related_name='children')

class Period(NamedTreeModel):
    parent = TreeForeignKey('Period', null=True, blank=True, 
        related_name='children')

class RepresentationSource(NamedTreeModel):
    parent = TreeForeignKey('RepresentationSource', null=True, blank=True, 
        related_name='children')

class RepresentationSubject(NamedTreeModel):
    parent = TreeForeignKey('RepresentationSubject', null=True, blank=True, 
        related_name='children')

class School(NamedTreeModel):
    parent = TreeForeignKey('School', null=True, blank=True, 
        related_name='children')

class StyleEra(NamedTreeModel):
    parent = TreeForeignKey('StyleEra', null=True, blank=True, 
        related_name='children')

class UsageDestination(NamedTreeModel):
    parent = TreeForeignKey('UsageDestination', null=True, blank=True, 
        related_name='children')

# must be last because it calls get_model
enable_custom_values(Artwork)
