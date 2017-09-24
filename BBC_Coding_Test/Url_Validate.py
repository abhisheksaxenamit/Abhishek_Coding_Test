import re
from urllib.parse import urlparse
import string
import tldextract
import sys


def contains_invalid(uri_set):
    '''
        Function to Check whether 'uri' contains ANY of the invalid characters
        Args:
            set of elements present in the uri
        Returns:
            True: If Invalid characters are Present
            False: None of the invalid characters are present.
    '''  
    inv_char = ['<' ,'>', '\"','#','{', '}', '|', '\\', '^', '~', '[', ']',  '`']
    for c in inv_char:
        if c in uri_set:
            print('Uri contains invalid char',c,file=sys.stderr)
            return True
    return False

def is_valid_ipv4(ipv4):
    '''
        Checking is the ip address is valid
        Args
            ipv4: ip address in string format
        Returns:
            True: if ip address is valid
            False: if ip address is invalid
    '''
    count=0;
    for val in re.split('\.',ipv4):
        if(int(val)>=256 or int(val)<0):
            print('IP address is out of range, '+val+' in ip '+ipv4, file=sys.stderr)
            return False
        count += 1
        if(count>4):
            return False
    if(count != 4):
        return False
    return True

def is_valid_port(port):
    '''
        Validating the port number is in the range 0 to 65535
        Args:
            port: port number
        Return
            True: valid port number
            False: invalid port number
    '''
    if(port > 65535 or port < 0):
        return False
    return True

    
def validate_url(url):
    '''
        Function to Validate the Url i.e if the url is valid or not.
        checks made:
            - scheme has either http, https or ftp
            - No invalid character is present (calling func contains_invalid)
            - Tld is correct i.e .com, .net, co.uk ...

        Args:
            url: The url that needs to be tested
        Returns:
            True: If Url is valid.
            False: Url in invalid.
    '''
    up = urlparse(url)
    try:
        # To check if scheme and url is present.
        assert all ([up.scheme, up.netloc])
        # checking if scheme is correct
        assert up[0] in ['http', 'https', 'ftp']
        # checking if any of the invalid characters are present in the url
        if(contains_invalid(set(url))):
            return False
        
        # Validating ipv4 address and port number in uri
        if(up.port):
            ipv4_chk= re.match(r'^\d+\.\d+\.\d+\.\d+:\d+$',up.netloc)
            if(ipv4_chk):
                if(is_valid_ipv4(ipv4_chk.group(0))==False):
                    return False
            if(is_valid_port(int(up.port)==False)):
                return False
        else:
            ipv4_chk= re.match(r'^\d+\.\d+\.\d+\.\d+$',up.netloc)
            if(ipv4_chk):
                if(is_valid_ipv4(ipv4_chk.group(0))==False):
                    return False
    except AssertionError:
        print("Assertion Error for Uri ",url,file=sys.stderr)
        return False
    except Exception as e:
        print(e,file = sys.stderr)
        return False
    return True


def status_code_lst(sc,sc_lst):
    '''
        Function to create the list for summary document. This will count the occurrance of Status_Code.
        eg. {
                Status_code : 200
                Number_of_responses
            }
        This code will either increment the existing Status code list or will add new status code 
        Args:
            sc: The new Status code recieved in the response
            sc_lst: The existing list of source code that needs to be updated.
        Return:
            sc_lst: The updated source code list.
    '''
    fnd = 0
    print("Status_Code: ",sc)
    try:
        for l in sc_lst:
            if(sc == l['Status_code']):
                fnd = 1
                l['Number_of_responses'] += 1
        if(fnd == 0):
            sc_lst.append({'Status_code': sc, 'Number_of_responses': 1})
    except Exception as e:
        print('ERROR:', e)
    return sc_lst
        
