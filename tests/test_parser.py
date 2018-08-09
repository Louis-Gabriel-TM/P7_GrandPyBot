#! /usr/bin/env python3
# coding: utf-8


import pytest

from parser import Parser


class TestParser:
    def setup(self):
        self.ps = Parser()

    def test_clean(self):
        assert self.ps.clean("") == ""


if __name__ == "__main__":
    pass

