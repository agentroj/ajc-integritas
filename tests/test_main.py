import unittest
# loading settings from .env file in root of project directory
from dotenv import load_dotenv
load_dotenv()

class QRTest(unittest.TestCase):
    """Tests for GeekTechStuff Grafana API Python"""
    '''

    def test_admin_name_is_string(self):
        admin_username = main.get_username()
        self.assertIs(type(admin_username),str)
    
    def test_admin_password_is_string(self):
        admin_password = main.get_password()
        self.assertIs(type(admin_password),str)
    
    def test_grafana_url_is_string(self):
        grafana_url = main.get_url()
        self.assertIs(type(grafana_url),str)
    
    def test_grafana_admin_url_is_string(self):
        admin_url = main.create_url()
        self.assertIs(type(admin_url),str)
    '''


    def test_infostring_is_string(self):
        psuid = "3425"
        acqid = "12312"
        paytype = '2436'
        merchid = "5436"
        merchcracc = "346"
        infostring  = f'00{len(psuid)}{psuid}01{len(acqid):02d}{acqid}02{len(paytype):02d}{paytype}03{len(merchid):02d}{merchid}04{len(merchcracc):02d}{merchcracc}'
        self.assertIs(type(infostring),str)
    
    def test_infostring_is_equal(self):
        psuid = "3425"
        acqid = "12312"
        paytype = '2436'
        merchid = "5436"
        merchcracc = "346"
        infostring  = f'00{len(psuid)}{psuid}01{len(acqid):02d}{acqid}02{len(paytype):02d}{paytype}03{len(merchid):02d}{merchid}04{len(merchcracc):02d}{merchcracc}'
        self.assertEqual(infostring, "004342501051231202042436030454360403346")
    
if __name__ == '__main__':
    unittest.main()