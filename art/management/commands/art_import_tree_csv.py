import csv

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from art import models

class Command(BaseCommand):
    args = '<joconde model class name> <file.csv>'
    help = 'Import a tree-ish csv file into a joconde table'

    def handle(self, *args, **options):
        model_class = getattr(models, args[0])
        r = csv.reader(open(args[1], 'U'), delimiter=',')

        current = []
        for row in r:
            i = 0
            for node in row:
                name = node.strip('", ').decode('utf-8')

                if name:
                    if '=' in name:
                        names = [x.strip() for x in name.split('=')]
                        name = '%s (%s)' % (names[0].strip(), ', '.join(names[1:]))

                    if i == 0:
                        model, created = model_class.objects.get_or_create(
                            name=name)
                    else:
                        model, created = model_class.objects.get_or_create(
                            name=name, parent=current[i-1])

                    if len(current) < i + 1:
                        current.append(model)
                    else:
                        current[i] = model

                i += 1
