#! /usr/bin/env python3
# coding: utf-8


import os
import requests

from .credentials import *


class GMapsRequest:
    URL_BASE = "https://maps.googleapis.com/maps/api/geocode/json?address="

    def __init__(self, parsed_request):
        self.question = ".".join(parsed_request.split())
        self.url = GMapsRequest.URL_BASE + self.question + \
            "&key=" + GMAPS_KEY

    def get_coord(self):
        api_data = self.get_data()
        try:
            return api_data['results'][0]['geometry']['location']
        except IndexError:
            return None

    def get_data(self):
        return requests.get(self.url).json()


def main():
    test = GMapsRequest("où trouve boulevard reine 78000 versailles")
    print()
    print("URL >>>", test.url)
    print()
    print("API_DATA >>>", test.get_data())
    print()
    print("COORD >>>",test.get_coord())


if __name__ == "__main__":
    main()
