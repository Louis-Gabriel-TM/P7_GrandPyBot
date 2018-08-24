#! /usr/bin/env python3
# coding: utf-8


"""
Robby the GrandPy Bot,
7th project of OC Python Developer Path.
Author: Loïc Mangin
"""


import requests


class WikiRequest:
    """This class handles request to Media Wiki API
    """
    BASE_PAGEID = "https://fr.wikipedia.org/w/api.php?" \
        + "action=query&prop=extracts&" \
        + "list=geosearch&gscoord={}|{}&gsradius=10000&" \
        + "gslimit=1&format=json"

    BASE_EXTRACT = "https://fr.wikipedia.org/w/api.php?" \
        + "action=query&pageids={}&prop=extracts&" \
        + "explaintext=true&exsectionformat=plain&" \
        + "exsentences=1&format=json"

    def __init__(self, latitude, longitude):
        """Takes coordinates to build the url to request
        """
        self.latitude = latitude
        self.longitude = longitude
        self.url_page_id = WikiRequest.BASE_PAGEID.format(
            self.latitude, self.longitude
            )

    def get_page_id(self):
        """Returns the id of a Wikipedia page to request
        to obtain an extract
        """
        wiki_data = requests.get(self.url_page_id)
        wiki_data = wiki_data.json()
        print("\nGET_PAGE_ID >>>", wiki_data)  # FOR DEBUG
        try:
            return wiki_data[
                'query']['geosearch'][0]['pageid']
        except IndexError:
            return ""
        except KeyError:
            return ""

    def get_extract(self):
        """Builds the url to request with the page id
        Returns an extract of the Wikipedia page
        """
        page_id = self.get_page_id()
        url_extract = WikiRequest.BASE_EXTRACT.format(page_id)
        wiki_data = requests.get(url_extract)
        wiki_data = wiki_data.json()
        print("\nGET_EXTRACT >>>", wiki_data)  # FOR DEBUG
        try:
            return wiki_data[
                'query']['pages'][str(page_id)]['extract']
        except IndexError:
            return ""
        except KeyError:
            return ""


def main():
    pass


if __name__ == "__main__":
    main()
