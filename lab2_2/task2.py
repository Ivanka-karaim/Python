import re


class TextFile:
    """"A class that performs statistical processing of a text file"""
    def __init__(self):
        self.symbol = 0
        self.words = 0
        self.sentences = 0
        try:
            self.f = open("file.txt", 'r')
        except IOError:
            raise IOError("file.txt is not found")

    def count_char(self):
        """"A function that counts the number of characters"""
        self.f.seek(0)
        data = self.f.read()
        self.symbol = len(data)
        return self.symbol

    def count_word(self):
        """"A function that counts the number of words"""
        self.f.seek(0)
        data = self.f.read()
        self.words = len(data.split())
        return self.words

    def count_sentence(self):
        """"A function that counts the number of sentences"""
        self.f.seek(0)
        data = self.f.read()
        self.sentences = len(re.split('\. |! |\? |\... ', data))
        return self.sentences

    def __del__(self):
        try:
            self.f.close()
        except IOError:
            raise IOError


x = TextFile()
print(x.count_char())
print(x.count_word())
print(x.count_sentence())

