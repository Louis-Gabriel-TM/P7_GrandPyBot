#! /usr/bin/env python3
# coding: utf-8


import pytest

from app.tools.parser import Parser


class TestParser:
    def setup(self):
        self.ps = Parser()

    def test_clean_empty(self):
        assert self.ps.clean("") == ""

    def test_clean_punctuation(self):
        assert self.ps.clean("Où donc, dis-moi ?") == ""

    def test_clean_case(self):
        assert self.ps.clean(
            "Situe Maisons-Laffitte"
            ) == "situe maisons-laffitte"

    def test_clean_stopwords(self):
        assert self.ps.clean(
            "Dis-moi Robby, où se trouve la tour Eiffel ?"
            ) == "robby trouve tour eiffel"


if __name__ == "__main__":
    pass

