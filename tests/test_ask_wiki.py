#! /usr/bin/env python3
# coding: utf-8


import pytest
import requests_mock

from app.tools.ask_wiki import WikiRequest


# TESTS MAKING FAKE REQUESTS (Mocks) :

def test_empty():
    with requests_mock.Mocker() as m:
        empty = WikiRequest(None, None)
        m.get(empty.url_page_id, text="{}")
        assert empty.get_page_id() == ""

def test_eiffel():
    with requests_mock.Mocker() as m:
        eiffel = WikiRequest(48.85837009999999, 2.2944813) # Eiffel Tower
        result = '{"query": {"geosearch": [{"pageid": 4641538}]}}'
        m.get(eiffel.url_page_id, text=result)
        assert eiffel.get_page_id() == 4641538

'''
# TESTS MAKING REAL REQUESTS :

class TestWikiRequest:
    def setup(self):
        self.empty = WikiRequest(None, None)
        self.eiffel = WikiRequest(48.85837009999999, 2.2944813) # Eiffel Tower

    def test_get_pageid(self):
        assert self.empty.get_page_id() == ""
        assert self.eiffel.get_page_id() == 4641538

    def test_get_extract(self):
        #assert self.empty.get_extract() == ""
        #print(self.eiffel.get_extract())
        
        assert self.eiffel.get_extract() == """Le Jules Verne \
est un restaurant parisien situé au deuxième étage de la Tour Eiffel \
et spécialisé en cuisine française classique."""
'''


if __name__ == "__main__":
    pass