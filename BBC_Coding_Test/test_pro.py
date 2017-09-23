import unittest
import Url_Validate as uv


class TestUri(unittest.TestCase):

    def test_uri_no_scheme(self):
        ##Validating Uris with no scheme
        ##O/p Expected 0 i.e. uri is wrong        
        uri='bbc1234'
        result = uv.validate_url(uri)
        self.assertEqual(result, 0)

    def test_uri_wrong_scheme(self):
        ##Validating Uris scheme not in [http,https and ftp]
        ##O/p Expected 0 i.e. uri is wrong        
        uri='bbc://abc.com'
        result = uv.validate_url(uri)
        self.assertEqual(result, 0)

    def test_uri_no_netloc(self):
        ##Validating Uris with no netloc
        ##O/p Expected 0 i.e. uri is wrong        
        uri='http://bbc1234'
        result = uv.validate_url(uri)
        self.assertEqual(result, 0)
    
if __name__=='__main__':
    unittest.main()
