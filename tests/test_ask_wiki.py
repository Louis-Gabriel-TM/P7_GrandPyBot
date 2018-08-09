#! /usr/bin/env python3
# coding: utf-8


import pytest

from app.tools.ask_wiki import WikiRequest


class TestWikiRequest:
    def setup(self):
        self.empty = WikiRequest(None, None)
        self.request = WikiRequest(48.85837009999999, 2.2944813) # Eiffel Tower

    def test_get_pageid(self):
        assert self.empty.get_pageid == None
        assert self.request.get_pageid == 4641538

    def test_get_extract(self):
        assert self.empty.get_coord() == None
        assert self.request.get_coord() == "Le Jules Verne \
            est un restaurant parisien situé au deuxième étage \
            de la Tour Eiffel et spécialisé en cuisine française classique."


if __name__ == "__main__":
    pass