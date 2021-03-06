import re
from urllib.parse import urlparse
import string
import tldextract
import sys


def contains_invalid(url):
    '''
        Function to Check whether 'url' contains ANY of the invalid characters
        Args:
            url : str, the http url to be tested.
        Returns:
            True: If Invalid characters are Present
            False: None of the invalid characters are present.
    '''
    url_set = set(url)
    inv_char = ['<' ,'>', '\"','{', '}', '|', '\\', '^', '~', '[', ']','`',' ']
    for c in inv_char:
        if c in url_set:
            print('url '+ url + ' contains invalid char',c,file=sys.stderr)
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

def is_valid_port(p):
    '''
        Validating the port number is in the range 0 to 65535
        Args:
            port: port number
        Return
            True: valid port number
            False: invalid port number
    '''
    if(0 <= p <= 65535):
        return True
    return False

    
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
        assert up[0] in ['http', 'https']
        # checking if any of the invalid characters are present in the url
        if(contains_invalid(url)):
            return False
                    
        # Validating ipv4 address and port number in url
        if(re.match(r'^\d+\.\d+\.\d+\.\d+:\d+$',up.netloc)):
            # If port is present in the url           
            ipv4_chk = re.match(r'^\d+\.\d+\.\d+\.\d+:\d+$',up.netloc)
            if(ipv4_chk):
                ipv4_add = re.split(':',ipv4_chk.group(0))[0]
                if(is_valid_ipv4(ipv4_add)==False):
                    return False
            if(is_valid_port(int(up.port))==False):
                return False
        elif(re.match(r'^\d+\.\d+\.\d+\.\d+$',up.netloc)):
            # If no port is present in the url with ip
            ipv4_chk=re.match(r'^\d+\.\d+\.\d+\.\d+$',up.netloc)
            if(is_valid_ipv4(ipv4_chk.group(0))==False):
                return False
        else:
            
            #checking the netloc doesn't start or end with '.' or '-' e.x. .www.foo.bar.
            if(up.netloc[0] in ['.','-'] or up.netloc[-1] in ['.','-']):
                return False
            
            parse_netloc = tldextract.extract(up.netloc)
            # if no ip is present than a suffix must be present
            if(parse_netloc.suffix == '' or parse_netloc.domain==''):
                print("Suffix or domain missing",url,file=sys.stderr)
                return False
            elif(parse_netloc.domain[0] in ['-','.'] or parse_netloc.suffix[0] in ['-','.'] or parse_netloc.domain[-1] in ['-','.'] or parse_netloc.suffix[-1] in ['-','.']):
                print("Invalid Suffix or domain",file=sys.stderr)
                return False
            
    except AssertionError:
        print("Assertion Error for url ",url,file=sys.stderr)
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
            sc: int, The new Status code received in the response
            sc_lst: [], The existing list of source code that needs to be updated.
        Return:
            sc_lst: [], The updated source code list.
    '''
    fnd = 0
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
        
