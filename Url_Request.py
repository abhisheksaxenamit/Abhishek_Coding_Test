import requests
import json

## Trying to look at the information in Header and looking at Status Code
HeaderFile = open('Header.txt','w')
r = requests.get("http://google.com")
HeaderFile.write(str(r.headers))
data=dict(r.headers)
with open('Header.json', 'w') as outfile:
    json.dump(data, outfile)
##r = requests.get("bad://address")
#print("Res: ",r.content)
print("Code: ",r.status_code)

HeaderFile.close()
