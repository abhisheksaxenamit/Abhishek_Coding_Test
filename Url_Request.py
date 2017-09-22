import requests
import json
import Url_Validate as uv

## Storing json for only valid urls.
## Trying to look at the information in Header and looking at Status Code
##HeaderFile = open('Header.txt','w')
##Output={}
count=0
s_code={}
time_out=0
data={}
sc_lst=[{'Status_Code': 200, 'Number_of_responses': 0},{'Status_Code': 404, 'Number_of_responses': 0}]
with open('Input.txt','r') as inp:
    for url in inp:
    ## removing white spaces in the end of the line      
        url=url.rstrip()
        try:
            if(uv.validate_url(url)):
##                print("Url Validated")
                try:
                    r = requests.get(url, timeout=10)
                except requests.exceptions.Timeout:
                    print("TIMEOUT!!!")
                    time_out=1
                if(time_out == 0):
                    sc_lst=uv.status_code_lst(r.status_code,sc_lst)
                    ##adding Url and Status Code
                    data={'Url' : url, 'Status_code' : r.status_code}
                    ## Checking if the field Content-Length is present in the header
                    try:
                        data.update({'Content_length' : r.headers['Content-Length']})
                    except:
                        data.update({'Content_length' : ''})
                    try:
                        data.update({'Date' : r.headers['Date']})
                    except:
                        data.update({'Date' : ''})
            else:
                data={'Url' : url, 'Error' : 'Invalid url'}
            ##Writing into the Json file
            f_name= 'Url_'+str(count)+'.json'
            count=count+1
##            print(f_name)
            with open(f_name, 'w') as outfile:
                json.dump(data, outfile)
            with open('Summary.json','w') as s:
                json.dump(sc_lst,s)
        except:
                print("ERROR!!")
