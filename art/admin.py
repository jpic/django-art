from django.contrib import admin

from models import *

class OeuvreAdmin(admin.ModelAdmin):
    raw_id_fields = (
        'author',
        'school',
        'period',
        'absolute_dating',
        'style_era',
        'original_copy_period',
        'legal_state',
        'creation_locations',
    )

admin.site.register(Oeuvre, OeuvreAdmin)
admin.site.register(GeographicalLocation)
admin.site.register(Inscription)
admin.site.register(School)
admin.site.register(StyleEra)
admin.site.register(Domain)
admin.site.register(Author)
admin.site.register(LegalState)
admin.site.register(Period)
admin.site.register(Dating)
