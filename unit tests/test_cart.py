import imp
from operator import mod
from tkinter import Button
import unittest
from unittest import result

from basket.models import Basket


class test_search_bar(unittest.TestCase):
    search_bar_obj = models()

    def setUp(self):
        self.sign_in_obj = models()

    def tearDown(self):
        del self.search_bar_obj

    def test_working_cart(self):

        Button = "Add To Cart"
        result = ["Your shopping basket", "checkout", "total", "Apply a voucher", "pay with card", "continue shopping"]

        output = self.sign_in_obj.working_cart(result)

        self.assertEquals(Button, result)

    def test_payment_system(self):

        Button = "Pay with card"
        Result = ["email", "name", "address", "city", "country"]

        output = self.sign_in_obj.payment_system(result)

        self.assertEquals(Button, Result)


    def test_payment_information_page(self):

        Button = "Payment info"
        result = ["card number", "MM/YY", "CVC"]

        output = self.sign_in_obj.information_page(result)

        self.assertEquals(Button, result)

    def test_invalid_payment_info(self):

        input = "1000100010001000 33/01 676"
        result = "*payment won't work"

        output = self.sign_in_obj.payment_info(result)

        self.assertEquals(input, result)

    def test_valid_payment_info(self):

        input = "4242424242424242 12/34 123"
        result = "✔ (movie is purchased)"

        output = self.sign_in_obj.payment_info(result)

        self.assertEquals(input, result)

