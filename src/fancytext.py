import random
from pyfiglet import Figlet


class Fancytext:
    def __init__(self, str, font):
        self.str = str
        self.font = font

    def print_text(self):
        custom_fig = Figlet(font=self.font)
        print(custom_fig.renderText(self.str))
