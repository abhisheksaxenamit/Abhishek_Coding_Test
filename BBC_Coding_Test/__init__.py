import requests
import json
import Url_Validate as uv
import sys

'''
    Storing json for only valid urls.
    Trying to look at the information in Header and looking at Status Code
'''
count = 0
s_code = {}
time_out = 0
data = {}
sc_lst = [{'Status_code': 200, 'Number_of_responses': 0},{'Status_code': 404, 'Number_of_responses': 0}]
# Reading data from the Input.txt file
with open('../Input.txt','r') as inp:
    for url in inp:
    # removing white spaces in the end of the line      
        url = url.rstrip()
        try:
            if(uv.validate_url(url)):
                try:
                    r = requests.get(url, timeout = 10)
                except requests.exceptions.Timeout:
                    print("Timeout Occurred for uri ",url,file = sys.stderr)
                    time_out = 1
                if(time_out == 0):
                    sc_lst=uv.status_code_lst(r.status_code,sc_lst)
                    # adding Url and Status Code
                    data={'Url' : url, 'Status_code' : r.status_code}
                    # Checking if the field Content-Length is present in the header
                    try:
                        data.update({'Content_length' : r.headers['Content-Length']})
                    except:
                        data.update({'Content_length' : ''})
                    # Checking if the field Date is present in the header
                    try:
                        data.update({'Date' : r.headers['Date']})
                    except:
                        data.update({'Date' : ''})
            else:
                data={'Url' : url, 'Error' : 'Invalid url'}
            # Writing into the Json file
            f_name= '../output/Url_' + str(count) + '.json'
            count=count+1
            with open(f_name, 'w') as outfile:
                json.dump(data, outfile)
            with open('../output/Summary.json','w') as s:
                json.dump(sc_lst,s)
        except Exception as e:
                print(e,file=sys.stderr)
