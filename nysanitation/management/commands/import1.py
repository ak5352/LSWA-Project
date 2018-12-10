from django.core.management.base import BaseCommand
import csv
from nysanitation.models import resturant

class Command(BaseCommand):
    def handle(self, *args, **options):
        f = open("export.csv")
        t = True
        i = 0
        for line in csv.reader(f):
            if (i > 100):
                break
            i+=1
            if (t):
                t = False
                continue
            foo = resturant(name=line[1], cuisine=line[7], score=line[13], borough=line[2], violation=line[11])
            try:
                foo.save()
            except Exception as e:
                print(e)
                continue
