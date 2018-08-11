#! /usr/bin/env python3
# coding: utf-8


import pytest

from app.tools.ask_gmaps import GMapsRequest


class TestGMapsRequest:
    def setup(self):
        self.empty = GMapsRequest("")
        self.eiffel = GMapsRequest("robby trouve tour eiffel")

    def test_get_coord(self):
        assert self.empty.get_coord() == None
        assert self.eiffel.get_coord() == {
            'lat': 48.85837009999999, 
            'lng': 2.2944813
            } # Eiffel Tower coordinates


if __name__ == "__main__":
    pass