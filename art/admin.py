from django.contrib import admin
from django.conf import settings
from django.utils.safestring import mark_safe

from orderable.admin import OrderableStackedInline, OrderableTabularInline

from models import *

class CommonMedia:
  js = (
    'https://ajax.googleapis.com/ajax/libs/dojo/1.6.0/dojo/dojo.xd.js',
    settings.STATIC_URL + '/orderable/orderable.js',
  )
  css = {
    'all': ( settings.STATIC_URL + '/art/editor.css',),
  }

class AudioInline(OrderableTabularInline):
    model = Audio
class ImageInline(OrderableTabularInline):
    model = Image
class VideoInline(OrderableTabularInline):
    model = Video

class ArtworkAdmin(admin.ModelAdmin):
    raw_id_fields = (
        'denomination',
        'artist',
        'school',
        'period',
        'style_era',
        'original_copy_period',
        'representation_subject',
        'representation_source',
        'creation_state',
        'creation_locations',
        'usage',
        'usage_period',
        'collect_method',
        'legal_state',
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
