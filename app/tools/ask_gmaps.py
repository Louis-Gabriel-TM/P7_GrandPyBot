#! /usr/bin/env python3
# coding: utf-8


import os
import requests

from app.tools.credentials import GMAPS_KEY
#from credentials import GMAPS_KEY


class GMapsRequest:
    URL_BASE = "https://maps.googleapis.com/maps/api/geocode/json?address="

    def __init__(self, parsed_request):
        #print("GMAPS_KEY =", GMAPS_KEY)
        self.question = ".".join(parsed_request.split())
        self.url = GMapsRequest.URL_BASE + self.question + \
            "&key=" + GMAPS_KEY

    def get_coord(self):
        api_data = self.get_data()
        try:
            return api_data['results'][0]['geometry']['location']
        except IndexError:
            return ""
        except KeyError:
            return ""
        return ""

    def get_data(self):
        gmaps_data = requests.get(self.url)
        print("GMAPS DATA >>>", gmaps_data)
        return gmaps_data.json()


#class Mock


def main():
    test = GMapsRequest("Dis-moi Robby, où se trouve la tour Eiffel ?")
    print("\nREQUEST URL >>>", test.url,
          "\n\nAPI_DATA >>>", test.get_data(),
          "\n\nCOORD >>>",test.get_coord()
          )


if __name__ == "__main__":
    main()
