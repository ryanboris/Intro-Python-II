from fancytext import Fancytext
from player import Player
from rooms import room as room


def beginGame():
    welcome_msg = Fancytext('Welcome!', 'weird').print_text()
    player_name = input('\nWhat is your name?\n')
    current_player = Player(player_name, room['outside'])
    print(f'Welcome, {current_player.name}.\nLet\'s begin.\n')
