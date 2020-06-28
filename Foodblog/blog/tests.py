from django.test import TestCase
from selenium import webdriver
import selenium, os, pathlib

def file_url(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

driver = webdriver.Chrome("chromedriver.exe")


# Create your tests here.
class WebpageTest(TestCase):

    def test_title(self):
        driver.get(file_url("blog/home.html"))
        self.assertEqual(driver.title, "Sweet eats | Home")