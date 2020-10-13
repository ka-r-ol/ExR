from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# https://requests.readthedocs.io/en/master/user/authentication/
from requests.auth import HTTPBasicAuth
import requests

import time
import scripts.load

HOME_URL = 'http://localhost:8000'
TEST_USER = 'karol'
TEST_USER_PASS = 'Pass4karol!'

"""
    # Functional tests are initially commented out 
    # due to a need of Chrome and chrome selenium driver 
    # installation

# https://selenium-python.readthedocs.io/locating-elements.html
class FunctionalTestCase(TestCase):

    def setUp(self):
        print("-->START: Functional tests")
        self.browser = webdriver.Chrome()

        scripts.load.run()    # loads sample data to test database

        suffix = '/admin/logout/'
        self.browser.get(HOME_URL+suffix)
        self.browser.get(HOME_URL+suffix)

        elem = self.browser.find_element_by_name("username")
        elem.clear()
        elem.send_keys(TEST_USER)

        elem = self.browser.find_element_by_name("password")
        elem.clear()
        elem.send_keys(TEST_USER_PASS)
        elem.send_keys(Keys.RETURN)
        # time.sleep(1)

    def tearDown(self):
        suffix = '/admin/logout/'
        self.browser.get(HOME_URL+suffix)
        self.browser.quit()
        print("-->END: Functional tests")

    def test_webpages_opens(self):

        for suffix, search_texts in [
            ('/api/v1/spots/', ['Spot List', 'Bajeczne MTV']),
            ('/api/v1/channels/', ['Channel List', 'TV Tomorrow']),
            ('/api/v1/spots/new', ['Spot Create'])
        ]:
            self.browser.get(HOME_URL+suffix)
            # time.sleep(1)
            print(f"checking {suffix}", end="")
            for text in search_texts:
                self.assertIn(text, self.browser.page_source)
            print(" - OK")

"""


class RestUnitTestCase(TestCase):
    def setUp(self):
        print("-->START: REST unit tests")
        self.auth = HTTPBasicAuth(TEST_USER, TEST_USER_PASS)

    def tearDown(self):
        print("-->END: REST unit tests")

    def test_get_channels(self):
        # https://www.pythonforbeginners.com/requests/using-requests-in-python class RequestUnitTestCase(TestCase): def test_get_channels(self): suffix = '/api/v1/channels'
        suffix = '/api/v1/channels/'
        r = requests.get(HOME_URL+suffix, auth=self.auth)
        self.assertEquals(r.status_code, 200)

    def test_get_spots(self):
        suffix = '/api/v1/spots/'
        r = requests.get(HOME_URL+suffix, auth=self.auth)
        self.assertEquals(r.status_code, 200)

    def test_post_spot(self):
        suffix = '/api/v1/spots/new'
        data = {
            "name": "Hello World",
            "price": "201.20",
            "start_time": "2020-09-01T03:30",
            "end_time": "2020-09-02T03:33",
            "channel": "TV Tomorrow"
        }
        r = requests.post(HOME_URL+suffix, auth=self.auth, data=data)
        if r.status_code == 201:
            print(f"Record created in database:\n{r.json()}")
        self.assertEquals(r.status_code, 201)


class DatabaseUnitTestCase(TestCase):

    def setUp(self):
        print("-->START: DB unit tests")
        scripts.load.run()    # loads sample data to test database

    def tearDown(self):
        print("-->END: DB unit tests")
        pass

    def test_check_users(self):
        for username, password in [
            ('karol', 'Pass4karol!'),
            ('jakub', 'Pass4jakub!')
        ]:
            user = authenticate(username=username, password=password)
            print(f"logged user={user}")
            self.assertIsNotNone(user)
