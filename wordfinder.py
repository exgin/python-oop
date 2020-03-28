import random


class WordFinder:
    """Finding random words in a dictionary

    >>> wf = WordFinder("simple.txt")
        3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
        True
    """

    def __init__(self, path):
        """Read dictionary and reports # items read."""
        dict_file = open(path)
        self.words = self.parse(dict_file)

        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Parse dict_file -> list of words."""
        return [letter.strip() for letter in dict_file]

    def random(self):
        """Return a random word"""
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """Find a special word

    >>> swf = SpecialWordFinder("complex.txt")
    4 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    """

    def parse(self, dict_file):
        """Parse dict_file -> list of words, skipping blanks/comments."""
        return [letter.strip() for letter in dict_file]


wf = WordFinder("simple.txt")
print(wf.random() in ["cat", "dog", "porcupine"])


swf = SpecialWordFinder("complex.txt")
print(swf.random() in ["pear", "carrot", "kale"])
