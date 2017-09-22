import re
from urllib.parse import urlparse
import string

def validate_url(url):
    print("Url: ", url)
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
    print("Url Valid!!")
    return 1

def source_code(sc):
    print("Source_Code: ",sc)
