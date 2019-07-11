import random
from pyfiglet import Figlet


class Puzzle:
    def __init__(self, str1, font):
        self.str1 = str1
        self.font = font

    def shuffle(self):
        mystery_phrase = self.str1
        self.new_str = ''
        self.split_phrase = [char for char in mystery_phrase]
        random.shuffle(self.split_phrase)
        for char in self.split_phrase:
            self.new_str += char
        return self.printShuffled(self.new_str)

    def printShuffled(self, s):
        custom_fig = Figlet(font=self.font)
        print(custom_fig.renderText(s))
