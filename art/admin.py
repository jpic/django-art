from django.contrib import admin

from models import *

class AudioInline(admin.TabularInline):
    model = Audio
class ImageInline(admin.TabularInline):
    model = Image
class VideoInline(admin.TabularInline):
    model = Video

class ArtworkAdmin(admin.ModelAdmin):
    raw_id_fields = (
        'denomination',
        'author',
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

    inlines = [
        AudioInline,
        ImageInline,
        VideoInline,
    ]

admin.site.register(Artwork, ArtworkAdmin)
admin.site.register(Author)
admin.site.register(CollectMethod)
admin.site.register(CreationState)
admin.site.register(Denomination)
admin.site.register(Domain)
admin.site.register(InscriptionType)
admin.site.register(GeographicalLocation)
admin.site.register(LegalState)
admin.site.register(MaterialTechnique)
admin.site.register(Period)
admin.site.register(RepresentationSource)
admin.site.register(RepresentationSubject)
admin.site.register(School)
admin.site.register(StyleEra)
admin.site.register(UsageDestination)
