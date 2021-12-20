from random_word import RandomWords

from generator.name_provider.name_provider import NameProvider


class RandomNameProvider(NameProvider):
    def __init__(self):
        self.random_words = RandomWords()

    def get_name(self):
        w = self.random_words.get_random_word()
        while w is None:
            w = self.random_words.get_random_word()
        return w.split(" ")[0].lower().replace("-", "_")
