import unittest
import Url_Validate as uv
import sys


class TestUrl(unittest.TestCase):

    def test_url_no_scheme(self):
        '''
            Validating urls with no scheme
            Output Expected 0 i.e. url is wrong
        '''
        url = 'bbc1234'
        result = uv.validate_url(url)
        try:
            self.assertEqual(result, 0)
            print("test_url_no_scheme : Pass", file = sys.stdout)
        except AssertionError:
            print("test_url_no_scheme : Failed", file = sys.stdout)
        except Exception as e:
            print("test_url_no_scheme : Failed", file = sys.stdout)
            print(e,file=sys.stderr)

    def test_url_wrong_scheme(self):
        '''
            Validating urls scheme not in [http,https and ftp]
            Output Expected 0 i.e. url is wrong
        '''
        url = 'bbc://abc.com'
        result = uv.validate_url(url)
        try:
            self.assertEqual(result, 0)
            print("test_url_wrong_scheme : Pass", file = sys.stdout)
        except AssertionError:
            print("test_url_wrong_scheme : Failed", file = sys.stdout)
        except Exception as e:
            print("test_url_wrong_scheme : Failed", file = sys.stdout)
            print(e,file=sys.stderr)
            

    def test_url_wrong_suffix(self):
        '''
            Validating urls with no netloc tld i.e .com, .net etc
            Output Expected 0 i.e. tld is wrong
        '''
        url='http://bbc1234'
        result = uv.validate_url(url)
        try:
            self.assertEqual(result, 0)
            print("test_url_wrong_suffix : Pass", file = sys.stdout)
        except AssertionError:
            print("test_url_wrong_suffix : Failed", file = sys.stdout)
        except Exception as e:
            print("test_url_wrong_suffix : Failed", file = sys.stdout)
            print(e,file=sys.stderr)

    def test_url_invalid_char(self):
        '''
            Validating urls with invalid characters
            Output Expected 0 i.e. invalid character present in the url
        '''
        url='http://bbc^.com'
        result = uv.validate_url(url)
        try:
            self.assertEqual(result, 0)
            print("test_url_invalid_char : Pass", file = sys.stdout)
        except AssertionError:
            print("test_url_invalid_char : Failed", file = sys.stdout)
        except Exception as e:
            print("test_url_invalid_char : Failed", file = sys.stdout)
            print(e,file=sys.stderr)

    def test_url_invalid_ipv4(self):
        '''
            Validating urls with invalid ip address
            Output Expected 0 i.e. invalid ip address present in the url
        '''
        url='http://1000.11.22.1/'
        result = uv.validate_url(url)
        try:
            self.assertEqual(result, 0)
            print("test_url_invalid_ipv4 : Pass", file = sys.stdout)
        except AssertionError:
            print("test_url_invalid_ipv4 : Failed", file = sys.stdout)
        except Exception as e:
            print("test_url_invalid_ipv4 : Failed", file = sys.stdout)
            print(e,file=sys.stderr)

    def test_url_invalid_port(self):
        '''
            Validating urls with invalid port number
            Output Expected 0 i.e. invalid port number present in the url
        '''
        url='http://192.168.22.1:65536/'
        result = uv.validate_url(url)
        try:
            self.assertEqual(result, 0)
            print("test_url_invalid_port : Pass", file = sys.stdout)
        except AssertionError:
            print("test_url_invalid_port : Failed", file = sys.stdout)
        except Exception as e:
            print("test_url_invalid_port : Failed", file = sys.stdout)
            print(e,file=sys.stderr)

    def test_url_valid_ipv4(self):
        '''
            Validating urls with valid ip address
            Output Expected 1 i.e. valid ip address is valid
        '''
        url='http://192.168.22.1/'
        result = uv.validate_url(url)
        try:
            self.assertEqual(result, 1)
            print("test_url_valid_ipv4 : Pass", file = sys.stdout)
        except AssertionError:
            print("test_url_valid_ipv4 : Failed", file = sys.stdout)
        except Exception as e:
            print("test_url_valid_ipv4 : Failed", file = sys.stdout)
            print(e,file=sys.stderr)
    
    def test_url_valid_url_port(self):
        '''
            Validating urls with valid port address
            Output Expected 1 i.e. valid address with port
        '''
        url='http://userid@example.com:8080'
        result = uv.validate_url(url)
        try:
            self.assertEqual(result, 1)
            print("test_url_valid_url_port : Pass", file = sys.stdout)
        except AssertionError:
            print("test_url_valid_url_port : Failed", file = sys.stdout)
        except Exception as e:
            print("test_url_valid_url_port : Failed", file = sys.stdout)
            print(e,file=sys.stderr)

    def test_url_valid_port(self):
        '''
            Validating urls with valid port number
            Output Expected 1 i.e. valid url and port number present in the url
        '''
        url='http://google.com:6553/'
        result = uv.validate_url(url)
        try:
            self.assertEqual(result, 1)
            print("test_url_valid_port : Pass", file = sys.stdout)
        except AssertionError:
            print("test_url_valid_port : Failed", file = sys.stdout)
        except Exception as e:
            print("test_url_valid_port : Failed", file = sys.stdout)
            print(e,file=sys.stderr)

    def test_new_status_code(self):
        '''
            Validating new status code is correctly added to the status list
            Output to verify is status code list is correctly updated
        '''
        sc_lst = [{'Status_code': 200, 'Number_of_responses': 2},{'Status_code': 404, 'Number_of_responses': 3}]
        #new status code
        sc=302
        sc_lst = uv.status_code_lst(sc,sc_lst)
        fnd = 0
        try:
            for l in sc_lst:
                if(sc == l['Status_code'] and l['Number_of_responses'] == 1):
                    fnd = 1
                    print("test_new_status_code : Pass", file = sys.stdout)
                    
            if(fnd == 0):
                print("test_new_status_code : Failed", file = sys.stdout)
        except Exception as e:
            print("test_new_status_code : Failed", file = sys.stdout)
            print(e,file=sys.stderr)
            


    def test_url_invalid_url_doc(self):
        '''
            Validating that all the urls in 'invalid_url.txt' are correctly processed.
            Output Expected 0 for all listed urls  i.e. all are invalid url.
        '''
        with open('../invalid_urls.txt','r') as inp:
            for url in inp:
                # removing white spaces in the end of the line
                url = url.rstrip()
                try:
                    result = uv.validate_url(url)
                    try:
                        self.assertEqual(result, 0)
                        print("test_url_invalid_url_doc url("+ url +"): Pass", file = sys.stdout)
                    except AssertionError:
                        print("test_url_invalid_url_doc url("+ url +") : Failed", file = sys.stdout)
                except Exception as e:
                    print(e,file=sys.stderr)
                    
if __name__ == '__main__':
    sys.stdout = open('../logs/unit_test_results.txt', 'w')
    sys.stderr = open('../logs/logs_testing.txt', 'a')
    unittest.main()
    sys.stderr.close()
    sys.stdout.close()
