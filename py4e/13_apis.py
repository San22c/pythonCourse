
#Call APIs google

import urllib.request, urllib.parse, urllib.error
import json

#https://maps.googleapis.com/maps/api/geocode/outputFormat?parameters
api_key = 42
serviceurl = input('Enter apis url:')
sparams = input('Enter address:')

#Complete url with attributes
parms = dict()
parms['address'] = sparams
parms['key'] = api_key

url = serviceurl + urllib.parse.urlencode(parms)
print('URL:',url)

########## CALL API AND TAKE RESPONSE
response = urllib.request.urlopen(url).read().decode()
print('Response:', response)
print('Type-response:', type(response))

##Conver to JSON
ijson = None
try:
    ijson = json.loads(response)
except:
    ijson = None
print('Type:',ijson)

if ijson == None or ijson['status'] != 'OK':
    print('############### FAILURE TO Retrieved #########')
    quit()
else:
    print('Solo la lista \n',ijson['results'])
    listado = list()
    for x in ijson['results']:
        for y in x['address_components']:
            listado.append(y['long_name'])
    print('Listado:', listado)
