from fancytext import Fancytext
from item import Item
from room import Room
from rooms import room as room
from player import Player
from puzzle import Puzzle
from beginning import beginGame

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['treasure'].n_to = room['meadows']
room['meadows'].s_to = room['mountain']
room['mountain'].e_to = room['cove']


def main():
    beginGame()


if __name__ == "__main__":
    main()
