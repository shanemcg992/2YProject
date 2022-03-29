import email
from re import I
from unicodedata import name
import unittest

from accounts.views import views

class test_sign_in(unittest.TestCase):
    sign_in_obj = views()

    def setUp(self):
        self.sign_in_obj = views()

    def tearDown(self):
        del self.sign_in_obj


    def test_create_user(self):

        details = "test1", "shanemcg992@gmail.com", "21", "laylabenji12", "laylabenji12"

        output = self.sign_in_obj.create_user(details)

        self.assertEquals(output, "User details:", details)


    def test_invalid_credentials(self):

        details = "test1", "shanemcg992@gmail.com", "21", "layla1", "layla1"
        error = "Password invalid. Password must be more than 8 characters long."
        
        output = self.sign_in_obj.create_user(error)

        self.assertEquals(details,"\n",error)

    
    def test_sign_in_valid_data(self):

        details = "project2", "Aaronfinnshane1"

        output = self.sign_in_obj.sign_in(details)

        self.assertEquals(output, "Welcome User:", details)

    def test_sign_in_invalid_data(self):

        details = "projec", "Aaronfinnshane1"

        error = "Please enter correct username or password"
        output = self.sign_in_obj.sign_in(error)

        self.assertEquals(error)

