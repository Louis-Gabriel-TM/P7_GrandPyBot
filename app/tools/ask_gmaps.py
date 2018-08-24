#! /usr/bin/env python3
# coding: utf-8


"""
Robby the GrandPy Bot,
7th project of OC Python Developer Path.
Author: Loïc Mangin
"""


import requests

from app.tools.credentials import GMAPS_KEY


class GMapsRequest:
    """This class handles request to Google Maps API
    """
    URL_BASE = "https://maps.googleapis.com/maps/api/geocode/json?address="

    def __init__(self, user_request):
        """Takes user request to build the url to request
        """
        self.question = ".".join(user_request.split())
        self.url = GMapsRequest.URL_BASE + self.question + \
            "&key=" + GMAPS_KEY

    def get_coord(self):
        """Extracts coordinates (latitude, longitude) from
        the data returned by Google Maps API
        """
        api_data = self.get_data()
        try:
            return api_data['results'][0]['geometry']['location']
        except IndexError:
            return ""
        except KeyError:
            return ""

    def get_data(self):
        """Requests the Google Maps API
        and returns data as a JSON object
        """
        gmaps_data = requests.get(self.url)
        print("GMAPS DATA >>>", gmaps_data.json())  # FOR DEBUG
        return gmaps_data.json()


def main():
    pass


if __name__ == "__main__":
    main()
