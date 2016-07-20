import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    # add address to url
    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url

    data = urllib.urlopen(url).read() # read this url
    print 'Retrieved', len(data), 'characters'

    try: js = json.loads(str(data)) # load json and check it
    except: js = None
    if 'status' not in js or js['status'] != 'OK': # check if wrong load
        print '==== Failure To Retrieve ===='
        print data
        continue

    #print json.dumps(js, indent=4) # print dump

    print 'Place id', js['results'][0]['place_id']
