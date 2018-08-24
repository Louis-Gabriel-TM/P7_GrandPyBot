#! /usr/bin/env python3
# coding: utf-8


"""
Robby the GrandPy Bot,
7th project of OC Python Developer Path.
Author: Loïc Mangin
"""


import json


class Parser:
    """This class provides a parser to keep only significant parts
    of the user query
    """
    def __init__(self):
        """Loads filters contained in the 'parsing_words.json' file
        A filter to retrieve punctuation
        Another to retrieve non significant words
        """
        with open('app/tools/parsing_words.json', encoding='utf-8') as f:
            parsing_words = json.loads(f.read())
        self.punctuation = parsing_words["punctuation"]
        self.stopwords = parsing_words["stopwords"]

    def clean(self, sentence):
        """Return the sentence with lower characters,
        without punctuation,
        without non significant words
        """
        sentence = sentence.lower()
        sentence = "".join(
            c for c in sentence if c not in self.punctuation)
        sentence = " ".join(
            w for w in sentence.split() if w not in self.stopwords)
        return sentence


if __name__ == "__main__":
    pass
