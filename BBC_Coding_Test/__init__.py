import requests
import json
import Url_Validate as uv
import sys

def create_json(fname,data):
    '''
        For creating a json file

        Args:
            fname = file name to be written
            data = data that needs to be dumped
    '''
    try:
        with open(fname, 'w') as outfile:
            json.dump(data, outfile)
    except Exception as e:
        print(e,file=sys.stderr)
        
    
def uri_resp(url,sc_lst,count):
    '''
        Validating the uri
        storing the response
        updating the status code summarry list

        Args:
            url = Uri thats needs to be processed
            sc_lst = existing status code list that needs to be updated
            count = the index of the url in the Input file.

        Return:
            sc_lst = updated status code list
    '''
    try:
        time_out = 0
        data = {}
        if(uv.validate_url(url)):
            try:
                r = requests.get(url, timeout = 2)
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
        create_json(f_name,data)
        return sc_lst
    except Exception as e:
            print(e,file=sys.stderr)
            return sc_lst
    
if __name__ == '__main__':
    '''
        Validating the urls 
        Storing important header information in json files.
        Creating a summary document to store the occurrance of Status Code
    '''
    sys.stderr = open('../logs/logs_error.txt', 'a')
    count = 0
    sc_lst = [{'Status_code': 200, 'Number_of_responses': 0},{'Status_code': 404, 'Number_of_responses': 0}]
    # Reading data from the Input.txt file
    with open('../Input.txt','r') as inp:
        for url in inp:
            # removing white spaces in the end of the line      
            url = url.rstrip()
            try:
                sc_lst=uri_resp(url,sc_lst,count)
                count += 1
                create_json('../output/Summary.json',sc_lst)
            except Exception as e:
                print(e,file=sys.stderr)
    sys.stderr.close()
