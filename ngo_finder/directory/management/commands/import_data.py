from django.core.management.base import BaseCommand
from django.db import transaction

from directory.data_importer import DataImporter

class Command(BaseCommand):

    @transaction.commit_on_success
    def handle(self,*args,**options):

        if args:
            data_file = args[0]
        di = DataImporter(data_file)
        di.go()
