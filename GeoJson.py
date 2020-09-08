import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

loc = input("Enter location: ")
encd = "http://py4e-data.dr-chuck.net/json?" + urllib.parse.urlencode({"address": loc, "key": 42})
#print(encd)
data = urllib.request.urlopen(encd, context = ctx).read()
#print(data)
print("Retrieving ", encd)
print("Retrieved ", len(data), "characters")

par = json.loads(data.decode())
if not par or 'status' not in par or par['status'] != 'OK':
    print('==== Failed To Retrieve ====')
#print(json.dumps(par, indent=4))
placeid = par["results"][0]["place_id"]
print("Place id ", placeid)
