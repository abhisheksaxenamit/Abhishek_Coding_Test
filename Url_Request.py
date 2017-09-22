import requests
import json

## Storing json for only valid urls.
## Trying to look at the information in Header and looking at Status Code
##HeaderFile = open('Header.txt','w')
##Output={}
count=0
with open('Input.txt','r') as inp:
    for url in inp:
##        url = inp.readlines()
        url=url.rstrip()
        print(url)
        try:
            r = requests.get(url)
            print("Code: ",r.status_code)
            if(r.status_code == 200):
                print("Code is 200 ")
            ##    HeaderFile.write(str(r.headers))
                data={'Url' : url, 'Status_code' : r.status_code}
                data.update(dict(r.headers))
            else:
                print("Code is not 200 ")
                data={'Url' : url, 'Status_code' : r.status_code}
    ##        with open('Header.json') as f:
    ##            Output = json.load(f)
##            Output.update(data)
        except:
            print("ERROR!!")

        f_name= 'Url_'+str(count)+'.json'
        count=count+1
        print(f_name)
        with open(f_name, 'w') as outfile:
            json.dump(data, outfile)
        ##r = requests.get("bad://address")
        #print("Res: ",r.content)
        

    ##HeaderFile.close()
