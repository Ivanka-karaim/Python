import re


class TextFile:
    """"A class that performs statistical processing of a text file"""
    def __init__(self, name_file):
        self.symbol = 0
        self.words = 0
        self.sentences = 0
        self.name_file = name_file

    def count_char(self):
        """"A function that counts the number of characters"""
        try:
            f = open(self.name_file, 'r')
            for line in f:
                self.symbol += len(line)
            f.close()
            return self.symbol
        except IOError:
            raise IOError("file.txt is not found")

    def count_word(self):
        """"A function that counts the number of words"""
        try:
            f = open(self.name_file, 'r')
            for line in f:
                self.words += len(list(filter(None, re.split(r'\w', line))))
            f.close()
            return self.words
        except IOError:
            raise IOError("file.txt is not found")

    def count_sentence(self):
        """"A function that counts the number of sentences"""
        try:
            f = open(self.name_file, 'r')
            for line in f:
                self.sentences += len(list(filter(None, re.split(r'\b[\.?!][A-Z\s+]', line))))
            f.close()
            return self.sentences
        except IOError:
            raise IOError("file.txt is not found")


x = TextFile("file.txt")
print(x.count_char())
print(x.count_word())
print(x.count_sentence())
