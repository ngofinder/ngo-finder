import csv
import sys
from directory.models import *

def create_geo_scope():
    cnt = Geo_scope.objects.count()
    if cnt == 0:
        gs = Geo_scope(id=1,scope='global').save()
        gs = Geo_scope(id=2,scope='country').save()
        gs = Geo_scope(id=3,scope='state/province').save()
        gs = Geo_scope(id=4,scope='county/district').save()
        gs = Geo_scope(id=5,scope='city/town').save()
        gs = Geo_scope(id=6,scope='postalcode').save()

def insert(csvrow):

    #############################################################
    # create object and populate its fields
    #org = Organization(name=orgname)
    org = Organization()
    org.name = csvrow[0]
    org.url = csvrow[8]

    if len(csvrow[6]) > 2:
        gsid = 5
    elif len(csvrow[5]) > 2:
        gsid = 4
    elif len(csvrow[4]) > 2:
        gsid = 3
    elif len(csvrow[3]) > 2:
        gsid = 2
    else:
        gsid = 1

    org.geo_scope = Geo_scope.objects.get(pk=gsid)

    #############################################################
    # save the object
    org.save()

    #############################################################
    # add sectors
    sectors = csvrow[1].lower().split(',')
    for sector in sectors:
        if len(sector) == 0:
            continue
        stripped = sector.strip()
        org.sectors.add(Sector.objects.get_or_create(sector=stripped)[0])

    #############################################################
    # create, populate and save the contact object
    insert_con = False
    con = Contact()
    if len(csvrow[9]) > 1:
        con.email = csvrow[9]
        insert_con = True
    if len(csvrow[10]) > 1:
        con.primary_phone = csvrow[10]
        insert_con = True
    if len(csvrow[11]) > 1:
        con.name = csvrow[11]
        insert_con = True
    if insert_con:
        con.organization = org
        con.save()

    #############################################################
    # create, populate and save the operation object
    op = Operation()
    if len(csvrow[3]) > 1:
        op.countries = csvrow[3]
    if len(csvrow[4]) > 1:
        op.states = csvrow[4]
    if len(csvrow[5]) > 1:
        op.counties = csvrow[5]
    if len(csvrow[6]) > 1:
        op.cities = csvrow[6]
    op.organization = org
    op.save()

    #############################################################
    # create, populate and save the location object
    addr = csvrow[7].split(',')

    if len(addr) == 6:
        loc = Location()
        if len(addr[0].strip()) > 1:
            loc.street = addr[0].strip()
        if len(addr[1].strip()) > 1:
            loc.city = addr[1].strip()
        if len(addr[2].strip()) > 1:
            loc.county = addr[2].strip()
        if len(addr[3].strip()) > 1:
            loc.state = addr[3].strip()
        if len(addr[4].strip()) > 1:
            loc.postal = addr[4].strip()
        if len(addr[5].strip()) > 1:
            loc.country = addr[5].strip()

        loc.organization = org
        loc.save()


create_geo_scope()
#ifile  = open("ZambiaNGOdatabase12022012.csv", "rb")
ifile  = open(sys.argv[1], "rb")
reader = csv.reader(ifile)

rownum = 0
for row in reader:
    rownum += 1
    if rownum == 1:
        header = row
        continue

    #print row[10]
    insert(row) 

ifile.close()

#sys.exit()

