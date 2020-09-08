import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter location: ")

data = urllib.request.urlopen(url, context = ctx).read()
print("Retrieving ", url)
print("Retrieved ", len(data), "characters")
par = json.loads(data)
sum = 0
count = 0

for ele in par["comments"]:
    sum += int(ele["count"])
    count += 1

print("Count: ", count)
print("Sum: ", sum)
