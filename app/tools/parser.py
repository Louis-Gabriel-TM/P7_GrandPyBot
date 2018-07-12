#! /usr/bin/env python3
# coding: utf-8


import json


class Parser:
    def __init__(self, words_file='app/tools/parsing_words.json'):
        with open(words_file, encoding='utf-8') as f:
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


def main():
    print("START")
    ps = Parser('parsing_words.json')
    test_sentences = [
        "",
        "Dites-moi, à qui est ce petit Bulldog dans la vitrine ?",
        "Où se trouve le Boulevard de la Reine 78 000 Versailles ?",
        "Montre-moi le 14, avenue des Champs-Elysées ?",
        "5, rue du boulevard de Paris 75014"
        ]
    for sentence in test_sentences:
        print()
        print(sentence)
        print(ps.clean(sentence))


if __name__ == "__main__":
    main()
