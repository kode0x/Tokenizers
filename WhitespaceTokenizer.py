import re

class WhitespaceTokenizer:
    def __init__(self, text):
        self.text = text
        self.vocab = {}
        self.nextIndex = 0

    def tokenize(self):
        return re.sub(r'\s+', ' ', self.text).strip().split(' ')

    def buildVocab(self):
        tokens = self.tokenize()
        for token in tokens:
            if token not in self.vocab:
                self.vocab[token] = self.nextIndex
                self.nextIndex += 1

    def encode(self):
        self.buildVocab()
        tokens = self.tokenize()
        return [self.vocab[token] for token in tokens]

    def decode(self, encodedText):
        reverse_vocab = {index: token for token, index in self.vocab.items()}
        return ' '.join([reverse_vocab[index] for index in encodedText])