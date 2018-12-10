from django.core.management.base import BaseCommand
import csv
from nysanitation.models import resturant

class Command(BaseCommand):
    def handle(self, *args, **options):
        f = open("export.csv")
        t = True
        i = 0
        for line in csv.reader(f):
            if (t):
                t = False
                continue
            foo = resturant(name=line[1], cuisine=line[7], score=line[13], borough=line[2], address=line[3] + ", " + line[4], zipcode=line[5])
            try:
                foo.save()
            except Exception as e:
                print(e)
                continue
