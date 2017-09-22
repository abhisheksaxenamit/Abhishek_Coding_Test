import re
from urllib.parse import urlparse
import string

## Function to Validate the Url
def validate_url(url):
##    print("Url: ", url)
    up = urlparse(url)
    try:
        assert all ([up.scheme, up.netloc])
        assert up[0] in ['http', 'https', 'ftp']
        assert set(up.netloc) <= set(string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation)
    except AssertionError:
##        print("Url InValid!!")
        return 0
    except Exception as e:
        print(e)
        return 0 
##    if(up[0] == '' or up[1] == ''):
##        print('INVALID URL : ',url)
##        return 0
##    print("Url Valid!!")
    return 1

##Function to count the number of Status_Code 
def status_code_lst(sc,sc_lst):
    fnd=0
    print("Status_Code: ",sc)
    try:
        for l in sc_lst:
            if(sc==l['Status_Code']):
                fnd=1
                l['Number_of_responses']+=1
        if(fnd==0):
            sc_lst.append({'Status_Code': sc, 'Number_of_responses': 0})
    except Exception as e:
        print('ERROR:', e)
    return sc_lst
        
