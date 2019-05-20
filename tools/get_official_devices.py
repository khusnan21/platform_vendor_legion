import json
try:
    # For python3
    import urllib.error
    import urllib.parse
    import urllib.request
except:
    # For python2
    import imp
    import urllib2
    import urlparse
    urllib = imp.new_module('urllib')
    urllib.error = urllib2
    urllib.parse = urlparse
    urllib.request = urllib2
try:
    url = "https://raw.githubusercontent.com/legionRom/platform_vendor_legion/pie/legion.devices.json"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    for res in data:
        print (res['codename'])
except:
    print ("")