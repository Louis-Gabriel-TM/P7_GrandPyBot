#! /usr/bin/env python3
# coding: utf-8


import json


class Parser:
    def __init__(self):
        with open('app/tools/parsing_words.json', encoding='utf-8') as f:
            parsing_words = json.loads(f.read())
        self.punctuation = parsing_words["punctuation"]
        self.stopwords = parsing_words["stopwords"]
        #self.way_types = parsing_words["way_types"] 

    def clean(self, sentence):
        sentence = sentence.lower()
        sentence = "".join(
            c for c in sentence if c not in self.punctuation)
        sentence =  " ".join(
            w for w in sentence.split() if w not in self.stopwords)
        return sentence


if __name__ == "__main__":
    pass
