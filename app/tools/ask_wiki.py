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
        self.url_page_id = WikiRequest.BASE_PAGEID.format(
            self.latitude, self.longitude
            )

    def get_page_id(self):
        wiki_data = requests.get(self.url_page_id)
        wiki_data = wiki_data.json()
        print("\nGET_PAGE_ID >>>", wiki_data)
        try:
            return wiki_data[
                'query']['geosearch'][0]['pageid']
        except IndexError:
            return ""
        except KeyError:
            return ""
        return ""

    def get_extract(self):
        page_id = self.get_page_id()
        url_extract = WikiRequest.BASE_EXTRACT.format(page_id)
        wiki_data = requests.get(url_extract)
        wiki_data = wiki_data.json()
        print("\nGET_EXTRACT >>>", wiki_data)
        try:
            return wiki_data[
                'query']['pages'][str(page_id)]['extract']
        except IndexError:
            return ""
        except KeyError:
            return ""
        return ""


def main():
    test = WikiRequest(48.85837009999999, 2.2944813) #Eiffel Tower
    print("\nPAGE ID >>>", test.get_page_id(),
          "\nEXTRACT >>>", test.get_extract())


if __name__ == "__main__":
    main()