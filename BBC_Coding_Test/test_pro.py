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
        except AssertionError:
            print("test_uri_no_scheme Test Case failed", file = sys.stderr)

    def test_uri_wrong_scheme(self):
        '''
            Validating Uris scheme not in [http,https and ftp]
            O/p Expected 0 i.e. uri is wrong
        '''
        uri = 'bbc://abc.com'
        result = uv.validate_url(uri)
        try:
            self.assertEqual(result, 0)
        except AssertionError:
            print("test_uri_wrong_scheme Test Case failed", file = sys.stderr)
            

    def test_uri_wrong_tld(self):
        '''
            Validating Uris with no netloc tld i.e .com, .net etc
            O/p Expected 0 i.e. tld is wrong
        '''
        uri='http://bbc1234'
        result = uv.validate_url(uri)
        try:
            self.assertEqual(result, 0)
        except AssertionError:
            print("test_uri_wrong_tld Test Case failed", file = sys.stderr)

    def test_uri_invalid_char(self):
        '''
            Validating Uris with invalid characters
            O/p Expected 0 i.e. invalid character present in the uri
        '''
        uri='http://bbc^.com'
        result = uv.validate_url(uri)
        try:
            self.assertEqual(result, 0)
        except AssertionError:
            print("test_uri_invalid_char Test Case failed", file = sys.stderr)

    def test_uri_invalid_ipv4(self):
        '''
            Validating Uris with invalid ip address
            O/p Expected 0 i.e. invalid ip address present in the uri
        '''
        uri='http://1000.11.22.1/'
        result = uv.validate_url(uri)
        try:
            self.assertEqual(result, 0)
        except AssertionError:
            print("test_uri_invalid_ipv4 Test Case failed", file = sys.stderr)

    def test_uri_invalid_port(self):
        '''
            Validating Uris with invalid port number
            O/p Expected 0 i.e. invalid port number present in the uri
        '''
        uri='http://192.168.22.1:6553/'
        result = uv.validate_url(uri)
        try:
            self.assertEqual(result, 0)
        except AssertionError:
            print("test_uri_invalid_port Test Case failed", file = sys.stderr)
    
if __name__ == '__main__':
    unittest.main()