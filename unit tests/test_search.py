import imp
import unittest

from search_app.admin import admin

class test_search_bar(unittest.TestCase):
    search_bar_obj = admin()

    def setUp(self):
        self.sign_in_obj = admin()

    def tearDown(self):
        del self.search_bar_obj


    def test_invalid_movie(self):

        search = "simpsons"
        output = "no results found"
        
        result = self.search_bar_obj.search(search)
        
        self.assertEquals(output, result)

    
    def test_valid_movie(self):

        search = "hal" or "halloween"
        output = "*film is displayed*"

        result = self.search_bar_obj.search(search)

        self.assertEquals(output, result)

