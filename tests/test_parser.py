#! /usr/bin/env python3
# coding: utf-8


import pytest

from app.tools.parser import Parser


class TestParser:
    def setup(self):
        self.ps = Parser()

    def test_clean(self):
        assert self.ps.clean("") == ""
        assert self.ps.clean("Où donc, dis-moi ?") == ""
        assert self.ps.clean("Paris") == "paris"
        assert self.ps.clean(
            "Dis-moi Robby, où se trouve la tour Eiffel ?"
            ) == "robby trouve tour eiffel"


if __name__ == "__main__":
    pass

