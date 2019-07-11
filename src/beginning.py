from fancytext import Fancytext
from player import Player
from rooms import room as room


class BeginGame:
    def __init__(self):
        self.welcome_msg = Fancytext('Welcome!', 'weird').print_text()
        self.player_name = input('\nWhat is your name?\n')
        self.current_player = Player(self.player_name, room['outside'])

    def print_beginning(self):
        self.welcome_msg
        self.player_name
        print(f'Welcome, {self.current_player.name}.\nLet\'s begin.\n')
