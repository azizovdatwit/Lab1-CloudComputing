import unittest
import requests
import json

class httpRequestsTest(unittest.TestCase):
    def test_getRoot(self):
        url = "http://localhost:8080/"
        response=requests.get(url)
        print("Response body:", response.json())
        self.assertEqual(200,response.status_code)

    def test_getAllHouses(self):
        url = "http://localhost:8080/houses"
        response = requests.get(url)
        print("Response Body:", response.json())
        self.assertEqual(200, response.status_code)

    def test_getHouseInfo(self):
        url = "http://localhost:8080/house/gryffindor"
        response = requests.get(url)
        print("Response Body:", response.json())
        self.assertEqual(200, response.status_code)

    def test_sortingHat(self):
        url = "http://localhost:8080/sortingHat?student=Harry"
        response = requests.get(url)
        print("Response Body:", response.json())
        self.assertEqual(200, response.status_code)

    def test_getMascot(self):
        url = "http://localhost:8080/house/slytherin/mascot"
        response = requests.get(url)
        print("Response Body:", response.json())
        self.assertEqual(200, response.status_code)

    def test_getFounder(self):
        url = "http://localhost:8080/house/ravenclaw/founder"
        response = requests.get(url)
        print("Response Body:", response.json())
        self.assertEqual(200, response.status_code)

    def test_getColors(self):
        url = "http://localhost:8080/house/hufflepuff/colors"
        response = requests.get(url)
        print("Response Body:", response.json())
        self.assertEqual(200, response.status_code)

    def test_getHead(self):
        url = "http://localhost:8080/house/gryffindor/head"
        response = requests.get(url)
        print("Response Body:", response.json())
        self.assertEqual(200, response.status_code)

    def test_bestCharacter(self):
        url = "http://localhost:8080/bestCharacter?person=Hermione"
        response = requests.get(url)
        print("Response Body:", response.json())
        self.assertEqual(200, response.status_code)

    def test_spells(self):
        url = "http://localhost:8080/spells?spell=Expelliarmus"
        response = requests.get(url)
        print("Response Body:", response.json())
        self.assertEqual(200, response.status_code)

    def test_readCookie(self):
        url = "http://localhost:8080/readcookie"
        cookies = {"username": "RonWeasley"}
        response = requests.get(url, cookies=cookies)
        print("Response Body:", response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.json()["username"], "RonWeasley")
