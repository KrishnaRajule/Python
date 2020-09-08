import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input("Enter the address: ")
print("Retrieving ", address)

xmlfile = urllib.request.urlopen(address, context = ctx)
data = xmlfile.read()
print("Retrieved ", len(data), "characters")

sum = 0
count = 0
tree = ET.fromstring(data)
result = tree.findall("comments/comment")

for ele in result:
    sum += int(ele.find("count").text)
    count += 1

print("Count: ", count)
print("Sum: ", sum)
