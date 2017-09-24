import unittest
import Url_Validate as uv
import sys


class TestUri(unittest.TestCase):

    def test_uri_no_scheme(self):
        '''
            Validating Uris with no scheme
            O/p Expected 0 i.e. uri is wrong
        '''
        uri = 'bbc1234'
        result = uv.validate_url(uri)
        try:
            self.assertEqual(result, 0)
            print("test_uri_no_scheme : Pass", file = sys.stdout)
        except AssertionError:
            print("test_uri_no_scheme : Failed", file = sys.stdout)

    def test_uri_wrong_scheme(self):
        '''
            Validating Uris scheme not in [http,https and ftp]
            O/p Expected 0 i.e. uri is wrong
        '''
        uri = 'bbc://abc.com'
        result = uv.validate_url(uri)
        try:
            self.assertEqual(result, 0)
            print("test_uri_wrong_scheme : Pass", file = sys.stdout)
        except AssertionError:
            print("test_uri_wrong_scheme : Failed", file = sys.stdout)
            

##    def test_uri_wrong_tld(self):
##        '''
##            Validating Uris with no netloc tld i.e .com, .net etc
##            O/p Expected 0 i.e. tld is wrong
##        '''
##        uri='http://bbc1234'
##        result = uv.validate_url(uri)
##        try:
##            self.assertEqual(result, 0)
##        except AssertionError:
##            print("test_uri_wrong_tld Test Case failed", file = sys.stderr)

    def test_uri_invalid_char(self):
        '''
            Validating Uris with invalid characters
            O/p Expected 0 i.e. invalid character present in the uri
        '''
        uri='http://bbc^.com'
        result = uv.validate_url(uri)
        try:
            self.assertEqual(result, 0)
            print("test_uri_invalid_char : Pass", file = sys.stdout)
        except AssertionError:
            print("test_uri_invalid_char : Failed", file = sys.stdout)

    def test_uri_invalid_ipv4(self):
        '''
            Validating Uris with invalid ip address
            O/p Expected 0 i.e. invalid ip address present in the uri
        '''
        uri='http://1000.11.22.1/'
        result = uv.validate_url(uri)
        try:
            self.assertEqual(result, 0)
            print("test_uri_invalid_ipv4 : Pass", file = sys.stdout)
        except AssertionError:
            print("test_uri_invalid_ipv4 : Failed", file = sys.stdout)

    def test_uri_invalid_port(self):
        '''
            Validating Uris with invalid port number
            O/p Expected 0 i.e. invalid port number present in the uri
        '''
        uri='http://192.168.22.1:65536/'
        result = uv.validate_url(uri)
        try:
            self.assertEqual(result, 0)
            print("test_uri_invalid_port : Pass", file = sys.stdout)
        except AssertionError:
            print("test_uri_invalid_port : Failed", file = sys.stdout)

    def test_uri_valid_ipv4(self):
        '''
            Validating Uris with valid ip address
            O/p Expected 1 i.e. valid ip address is valid
        '''
        uri='http://192.168.22.1/'
        result = uv.validate_url(uri)
        try:
            self.assertEqual(result, 1)
            print("test_uri_valid_ipv4 : Pass", file = sys.stdout)
        except AssertionError:
            print("test_uri_valid_ipv4 : Failed", file = sys.stdout)
    
    def test_uri_valid_uri_port(self):
        '''
            Validating Uris with valid port address
            O/p Expected 1 i.e. valid address with port
        '''
        uri='http://userid@example.com:8080'
        result = uv.validate_url(uri)
        try:
            self.assertEqual(result, 1)
            print("test_uri_valid_uri_port : Pass", file = sys.stdout)
        except AssertionError:
            print("test_uri_valid_uri_port : Failed", file = sys.stdout)

    def test_uri_valid_port(self):
        '''
            Validating Uris with valid port number
            O/p Expected 1 i.e. valid url and port number present in the uri
        '''
        uri='http://google.com:6553/'
        result = uv.validate_url(uri)
        try:
            self.assertEqual(result, 1)
            print("test_uri_valid_port : Pass", file = sys.stdout)
        except AssertionError:
            print("test_uri_valid_port : Failed", file = sys.stdout)

    def test_uri_invalid_uri_doc(self):
        '''
            Validating that all the uris in 'invalid_uri.txt' are correctly processed.
            O/p Expected 0 for all listed uris  i.e. all are invalid uri.
        '''
        with open('../invalid_uris.txt','r') as inp:
            for url in inp:
                # removing white spaces in the end of the line
                url = url.rstrip()
                try:
                    result = uv.validate_url(url)
                    try:
                        self.assertEqual(result, 0)
                        print("test_uri_invalid_uri_doc Uri("+ url +"): Pass", file = sys.stdout)
                    except AssertionError:
                        print("test_uri_invalid_uri_doc Uri("+ url +") : Failed", file = sys.stdout)
                except Exception as e:
                    print(e,file=sys.stderr)
                    
if __name__ == '__main__':
    sys.stdout = open('../logs/unit_test_results.txt', 'w')
    sys.stderr = open('../logs/logs_testing.txt', 'a')
    unittest.main()
    sys.stderr.close()
    sys.stdout.close()
