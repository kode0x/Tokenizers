class CharacterTokenizer:
    def __init__(self, text):
        self.text = text
        self.vocab = {}
        self.nextIndex = 0

    def tokenize(self, includeSpaces=False):
        if includeSpaces:
            return list(self.text)
        return [c for c in self.text if c != ' ']

    def buildVocab(self, includeSpaces=False):
        tokens = self.tokenize(includeSpaces)
        for token in tokens:
            if token not in self.vocab:
                self.vocab[token] = self.nextIndex
                self.nextIndex += 1

    def encode(self, includeSpaces=False):
        if not self.vocab:
            self.buildVocab(includeSpaces)
        tokens = self.tokenize(includeSpaces)
        return [self.vocab[token] for token in tokens]

    def decode(self, encodedText):
        """Decode list of indices back to text."""
        reverse_vocab = {index: token for token, index in self.vocab.items()}
        return ''.join([reverse_vocab[index] for index in encodedText])
