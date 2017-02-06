# -- coding: utf-8 --

import requests

#https://www.hurl.it/

searchfield = 'Berlin'
radius = 10000000
lon = 13.40495399
lat = 52.52000659

params = {'longitude': lon, 'latitude': lat, 'searchfield': searchfield, 'radius': radius}

req = requests.post('http://www.mcdonalds.de/search', params=params)

data = req.json()['restaurantList']

f = open('data.csv','w')
f.write('id' + '\t' + 'externalId' + '\t' + 'latitude' + '\t' + 'longitude' + '\t' + 'city' + '\t' + 'postalCode' + '\t' + 'address' + '\t' + 'street' + '\t' + 'phone' + '\t' + 'open24h' + '\t' + 'mcDrive' + '\t' + 'open24h' + '\t' + 'wlan' + '\t' + 'coupons' + '\t' + 'toggo' + '\t' + 'mcCafe' + '\t' + 'closedFrom' + '\t' + 'closedTo' + '\t' + 'seoURL' + '\t' + 'wednesday' + '\t' + 'sunday' + '\t' + 'thursday' + '\t' + 'friday' + '\t' + 'tuesday' + '\t' + 'saturday' + '\t' + 'monday' + '\t' + 'name1' + '\t' + 'name2' + '\n')

for item in data:
    id = item['restaurant']['id']
    externalId = item['restaurant']['externalId']
    latitude = item['restaurant']['latitude']
    longitude = item['restaurant']['longitude']
    city = item['restaurant']['city'].encode('utf-8')
    postalCode = item['restaurant']['postalCode']
    address = item['restaurant']['address'].encode('utf-8')
    street = item['restaurant']['street'].encode('utf-8')
    phone = item['restaurant']['phone']
    open24h = item['restaurant']['open24h']
    mcDrive = item['restaurant']['mcDrive']
    wlan = item['restaurant']['wlan']
    coupons = item['restaurant']['coupons']
    toggo = item['restaurant']['toggo']
    mcCafe = item['restaurant']['mcCafe']
    closedFrom = item['restaurant']['closedFrom']
    closedTo = item['restaurant']['closedTo']
    seoURL = 'https://www.mcdonalds.de/restaurant/' + item['restaurant']['seoURL'].encode('utf-8')
    wednesday = item['restaurant']['wednesday']
    sunday = item['restaurant']['sunday']
    thursday = item['restaurant']['thursday']
    friday = item['restaurant']['friday']
    tuesday = item['restaurant']['tuesday']
    saturday = item['restaurant']['saturday']
    monday = item['restaurant']['monday']
    name1 = item['restaurant']['name1'].encode('utf-8')
    name2 = item['restaurant']['name2'].encode('utf-8')

    record = str(id) + '\t' + str(externalId) + '\t' + str(latitude) + '\t' + str(longitude) + '\t' + str(city) + '\t' + str(postalCode) + '\t' + str(address) + '\t' + str(street) + '\t' + str(phone) + '\t' + str(open24h) + '\t' + str(mcDrive) + '\t' + str(open24h) + '\t' + str(wlan) + '\t' + str(coupons) + '\t' + str(toggo) + '\t' + str(mcCafe) + '\t' + str(closedFrom) + '\t' + str(closedTo) + '\t' + str(seoURL) + '\t' + str(wednesday) + '\t' + str(sunday) + '\t' + str(thursday) + '\t' + str(friday) + '\t' + str(tuesday) + '\t' + str(saturday) + '\t' + str(monday) + '\t' + str(name1) + '\t' + str(name2) + '\n'
    
    f.write(record)

f.close()


