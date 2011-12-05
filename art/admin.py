from django.contrib import admin
from django.conf import settings
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe

from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin

from orderable.admin import OrderableStackedInline, OrderableTabularInline

from admin_hack.admin import CustomValueInline

from lookups import *
from models import *

class CommonMedia:
  pass
  #js = (
    #'https://ajax.googleapis.com/ajax/libs/dojo/1.6.0/dojo/dojo.xd.js',
    #settings.STATIC_URL + '/orderable/orderable.js',
  #)
  #css = {
    #'all': ( settings.STATIC_URL + '/art/editor.css',),
  #}

class AudioInline(admin.TabularInline):
    model = Audio
    extra = 0
class ImageInline(admin.TabularInline):
    model = Image
    extra = 0
class VideoInline(admin.TabularInline):
    model = Video
    extra = 0

class ArtworkInline(admin.TabularInline):
    model = Artwork
    fields = ('name',)

class ArtworkAdmin(AjaxSelectAdmin):
    form = make_ajax_form(Artwork, {
        'artist': 'Artist',
        'collect_method': 'CollectMethod',
        'creation_state': 'CreationState',
        'denomination': 'Denomination',
        'domains': 'Domain',
        'inscription_types': 'InscriptionType',
        'creation_locations': 'GeographicalLocation',
        'legal_state': 'LegalState',
        'material_techniques': 'MaterialTechnique',
        'original_copy_period': 'Period',
        'usage_period': 'Period',
        'representation_subject': 'RepresentationSubject',
        'representation_source': 'RepresentationSource',
        'school': 'School',
        'style_era': 'StyleEra',
        'usage': 'UsageDestination',
    })

    fieldsets = (
        (None, {
            'fields': (
                (
                    'inventory_number',
                    'name',
                ),
                (
                    'old_inventory_number',
                    'other_inventory_numbers'
                ),
                (
                    'domains',
                    'denomination',
                ),
                (
                    'artist',
                    'school',
                    'previous_attributions',
                )
            )}
        ),
        (_(u'Datation'), {
            'classes': ('collapse',),
            'fields': (
                (
                    'period',
                    'vintage',
                ),
                'absolute_dating',
                'absolute_dating_details',
                'dating_laboratory',
                'style_era',
                'original_copy_period',
            )}
        ),
        (_(u'Description'), {
            'classes': ('collapse',),
            'fields': (
                'material_techniques',
                'dimensions',
                'inscription_types',
                'inscriptions_details',
                'onomastic',
                'description',
                'current_conservation_state',
                'representation_subject',
                'representation_details',
                'representation_date',
                'representation_source',
            )},
        ),
        (_(u'Historical context'), {
            'classes': ('collapse',),
            'fields': (
                'creation_state',
                'genes',
                'history',
                'creation_locations',
                'creation_locations_details',
                'geographical_history',
                'usage',
                'usage_details',
                'usage_locations',
                'usage_period',
                'usage_vintage',
                'origin',
                'collect_method',
                'origin_details',
                'sda_site_number',
            )}
        ),
        (_(u'Legal state'), {
            'classes': ('collapse',),
            'fields': (
                'legal_state',
                'acquisition_date',
                'previous_belonging',
                'previous_depots',
                'preservation_location',
                'acquisition_intermediary',
            )}
        ),
        (_(u'Additionnal informations'), {
            'classes': ('collapse',),
            'fields': (
                'bibliography',
                'exposure',
                'comments',
                'photograph',
                'editor',
                'copyright',
                'public',
            )},
        )
    )

    filter_horizontal = (
        'domains',
        'material_techniques',
        'inscription_types',
    )
    search_fields = (
        'name',
    )
    inlines = [
        AudioInline,
        ImageInline,
        VideoInline,
    ]
    date_hierarchy = 'creation_datetime'
    list_display = (
        'artwork_image',
        'name',
        'artist',
        'public',
    )
    list_filter = (
        'public',
    )
    list_display_links = (
        'artwork_image',
        'name',
    )
    list_editable = (
        'public',
    )
    list_select_related = True

    def artwork_image(self, obj):
        image = obj.first_image
        if not image:
            return
        else:
            return mark_safe(
                u'<img height="50px" src="%s" />' % image.media.url)
    artwork_image.short_description = 'image'
    artwork_image.allow_tags = True

admin.site.register(Artwork, ArtworkAdmin, Media=CommonMedia)

class ArtistAdmin(admin.ModelAdmin):
    list_display = (
        'artist_image',
        'name',
        'first_name',
        'last_name',
        'public',
    )
    search_fields = (
        'first_name',
        'last_name',
        'name',
        'group',
    )
    list_filter = (
        'public',
    )
    date_hierarchy = 'creation_datetime'
    list_display_links = (
        'artist_image',
        'name',
    )
    list_editable = (
        'public',
    )
    raw_id_fields = (
        'birth_city',
        'death_city',
    )

    def artist_image(self, obj):
        image = obj.image
        if not image:
            return
        else:
            return mark_safe(
                u'<img height="50px" src="%s" />' % image.url)
    artist_image.short_description = 'image'
    artist_image.allow_tags = True

admin.site.register(Artist, ArtistAdmin, Media=CommonMedia)

class NamedTreeModelAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
        'parent__name',
    )

admin.site.register(CollectMethod, NamedTreeModelAdmin)
admin.site.register(CreationState, NamedTreeModelAdmin)
admin.site.register(Denomination, NamedTreeModelAdmin)
admin.site.register(Domain, NamedTreeModelAdmin)
admin.site.register(InscriptionType, NamedTreeModelAdmin)
admin.site.register(GeographicalLocation, NamedTreeModelAdmin)
admin.site.register(LegalState, NamedTreeModelAdmin)
admin.site.register(MaterialTechnique, NamedTreeModelAdmin)
admin.site.register(Period, NamedTreeModelAdmin)
admin.site.register(RepresentationSource, NamedTreeModelAdmin)
admin.site.register(RepresentationSubject, NamedTreeModelAdmin)
admin.site.register(School, NamedTreeModelAdmin)
admin.site.register(StyleEra, NamedTreeModelAdmin)
admin.site.register(UsageDestination, NamedTreeModelAdmin)
