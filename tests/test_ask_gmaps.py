#! /usr/bin/env python3
# coding: utf-8


import pytest
import requests_mock

from app.tools.ask_gmaps import GMapsRequest


# TESTS MAKING FAKE REQUESTS (Mocks) :

def test_empty():
    with requests_mock.Mocker() as m:
        empty = GMapsRequest("")
        m.get(empty.url, text="{}")
        assert empty.get_coord() == ""

def test_eiffel():
    with requests_mock.Mocker() as m:
        eiffel = GMapsRequest("robby trouve tour eiffel")
        result = '{"results" : [{"geometry": {"location": \
            {"lat": 48.85837009999999, "lng": 2.2944813}}}]}'
        m.get(eiffel.url, text=result)
        assert eiffel.get_coord() == {
            'lat': 48.85837009999999, 
            'lng': 2.2944813
            }


'''
# TESTS MAKING REAL REQUESTS :

class TestGMapsRequest:
    def setup(self):
        self.empty = GMapsRequest("")
        self.non_sense = GMapsRequest("wyz iopww")
        self.eiffel = GMapsRequest("robby trouve tour eiffel")

    def test_get_coord(self):
        assert self.empty.get_coord() == ""
        assert self.non_sense.get_coord() == ""
        assert self.eiffel.get_coord() == {
            'lat': 48.85837009999999, 
            'lng': 2.2944813
            } # Eiffel Tower coordinates
'''


if __name__ == "__main__":
    pass