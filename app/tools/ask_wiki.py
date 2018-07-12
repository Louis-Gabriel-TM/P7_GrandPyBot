#! /usr/bin/env python3
# coding: utf-8


import requests

class WikiRequest:
    URL_BASE = "https://fr.wikipedia.org/w/api.php?" \
                + "action=opensearch&" \
                + "limit=1&search="

    def __init__(self, parsed_request):
        self.question = "|".join(parsed_request.split())
        self.url = WikiRequest.URL_BASE + self.question

    def get_data(self):
        return requests.get(self.url).json()

    def get_extract(self):
        api_data = self.get_data()
        try:
            return api_data[2][0]
        except IndexError:
            return None


def main():
    test = WikiRequest("où trouve ville versailles")
    print()
    print("URL >>>", test.url)
    print()
    print("API_DATA >>>", test.get_data())
    print()
    print("EXTRACT >>>", test.get_extract())


if __name__ == "__main__":
    main()