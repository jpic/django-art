import csv

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

try:
    from modeltranslation.translator import translator
except ImportError:
    translator = None

from art.models import *

class Command(BaseCommand):
    args = '<file.csv>'
    help = 'Import a tree-ish csv file into a joconde table'

    def handle(self, *args, **options):
        file_class_map = {
            'auteur': Author, # no parent
            'collect': CollectMethod,
            'stade-creation': CreationState,
            'denomination': Denomination,
            'domain': Domain,
            'inscriptions': InscriptionType,
            'lieu': GeographicalLocation,
            'juridique': LegalState,
            'techniques': MaterialTechnique,
            'datation': Period,
            'sources-representation': RepresentationSource,
            'sujet': RepresentationSubject,
            'ecole': School,
            'epoque': StyleEra,
            'utilisations': UsageDestination,
        }
        
        model_class = None
        for k, v in file_class_map.items():
            if k in args[0]:
                model_class = v
                break
        if not model_class:
            print "What to do with" + args[0]
            return

        r = csv.reader(open(args[0], 'U'), delimiter=',')

        current = []
        for row in r:
            i = 0
            for node in row:
                name = node.strip('", ').decode('utf-8')

                if name:
                    if '=' in name:
                        names = [x.strip() for x in name.split('=')]
                        name = '%s (%s)' % (names[0].strip(), ', '.join(names[1:]))

                    o = {}
                    try:
                        translator.get_options_for_model(model_class)
                        o['name_fr'] = name
                    except:
                        o['name'] = name

                    if i > 0:
                        o['parent'] = current[i-1]
                    
                    model, created = model_class.objects.get_or_create(**o)

                    if len(current) < i + 1:
                        current.append(model)
                    else:
                        current[i] = model

                i += 1
