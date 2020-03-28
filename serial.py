"""Word Finder: finds random words from a dictionary."""


class SerialGenerator:
    """Increment a number.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.reset()
    100
    """

    def __init__(self, start=0):
        """Make a new starting num"""
        self.start = self.next_num = start

    def __repr__(self):
        """Show our class representation"""
        return f"SerialGenerator start = {self.start} the next_num is = {self.next_num}"

    def addToStart(self):
        """Increment & return on next num"""
        self.next_num += 1
        return self.next_num - 1

    def reset(self):
        """Reset to the start num"""
        self.next_num = self.start


serial = SerialGenerator(start=100)
serial.addToStart()
print(serial)
