#! /usr/bin/env python3
# coding: utf-8


import requests

class WikiRequest:

    BASE_PAGEID = "https://fr.wikipedia.org/w/api.php?" \
                + "action=query&prop=extracts&" \
                + "list=geosearch&gscoord={}|{}&gsradius=10000&" \
                + "gslimit=1&format=json"

    BASE_EXTRACT = "https://fr.wikipedia.org/w/api.php?" \
                + "action=query&pageids={}&prop=extracts&" \
                + "explaintext=true&exsectionformat=plain&" \
                + "exsentences=1&format=json"

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.page_id = self.get_pageid()
        self.extract = self.get_extract()

    def get_pageid(self):
        url = WikiRequest.BASE_PAGEID.format(self.latitude, self.longitude)
        return requests.get(url).json()['query']['geosearch'][0]['pageid']

    def get_extract(self):
        url = WikiRequest.BASE_EXTRACT.format(self.page_id)
        return requests.get(url).json()[
                'query']['pages'][str(self.page_id)]['extract']


def main():
    test = WikiRequest(44.0, 1.0)

    print()
    print("PAGE ID >>>", test.page_id)
    print()
    print("EXTRACT >>>", test.extract)


if __name__ == "__main__":
    main()