import csv

from unesco.models import Category, State, Region, Iso, Site


def run():
    fhand = open('unesco/unesco.csv')
    reader = csv.reader(fhand)
    next(reader)

    Category.objects.all().delete()
    State.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()
    Site.objects.all().delete()

    for row in reader:
        print(row)

        cat, created = Category.objects.get_or_create(name=row[7])
        st, created = State.objects.get_or_create(name=row[8])
        reg, created = Region.objects.get_or_create(name=row[9])
        i, created = Iso.objects.get_or_create(name=row[10])


        try:
            yr = int(row[3])
        except:
            yr = None

        try:
            long = float(row[4])
        except:
            long = None

        try:
            lat = float(row[5])
        except:
            lat = None

        try:
            ah = float(row[6])
        except:
            ah = None





        site = Site(
            name = row[0],
            description = row[1],
            justification = row[2],
            year = yr,
            longitude = long,
            latitude = lat,
            area_hectares = ah,
            category = cat,
            state = st,
            region = reg,
            iso = i
        )
        site.save()