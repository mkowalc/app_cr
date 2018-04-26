import unittest
import os
import json
import requests
# from sources.api import app


class APITestCase(unittest.TestCase):

    #do uzupelnienia

    def test_basic_response(self):
        res = requests.get('http://0.0.0.0:5000')
        self.assertEqual(res.status_code, 200)


if __name__ == "__main__":
    unittest.main()