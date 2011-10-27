from modeltranslation.translator import translator, TranslationOptions

from models import *

class NameTranslation(TranslationOptions):
    fields = ('name',)

translator.register(CollectMethod, NameTranslation)
translator.register(CreationState, NameTranslation)
translator.register(Denomination, NameTranslation)
translator.register(Domain, NameTranslation)
translator.register(InscriptionType, NameTranslation)
translator.register(GeographicalLocation, NameTranslation)
translator.register(LegalState, NameTranslation)
translator.register(MaterialTechnique, NameTranslation)
translator.register(Period, NameTranslation)
translator.register(RepresentationSource, NameTranslation)
translator.register(RepresentationSubject, NameTranslation)
translator.register(School, NameTranslation)
translator.register(StyleEra, NameTranslation)
translator.register(UsageDestination, NameTranslation)
