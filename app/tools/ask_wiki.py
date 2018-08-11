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
        self.page_id = None
        self.extract = None

    def get_page_id(self):
        self.page_id = self._request_page_id()
        return self.page_id

    def get_extract(self):
        self.extract = self._request_extract()
        return self.extract

    def _request_page_id(self):
        url = WikiRequest.BASE_PAGEID.format(self.latitude, self.longitude)
        wiki_data = requests.get(url)
        wiki_data = wiki_data.json()
        try:
            return wiki_data[
                'query']['geosearch'][0]['pageid']
        except KeyError:
            return None

    def _request_extract(self):
        url = WikiRequest.BASE_EXTRACT.format(self.get_page_id())
        wiki_data = requests.get(url)
        wiki_data = wiki_data.json()
        try:
            return wiki_data[
                'query']['pages'][str(self.page_id)]['extract']
        except KeyError:
            return None


def main():
    test = WikiRequest(48.85837009999999, 2.2944813) #Eiffel Tower
    print("\nPAGE ID >>>", test.get_page_id(),
          "\nEXTRACT >>>", test.get_extract())


if __name__ == "__main__":
    main()