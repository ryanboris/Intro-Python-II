from fancytext import Fancytext
from item import Item
from items import items
from room import Room
from rooms import room as room
from player import Player
from puzzle import Puzzle
from beginning import BeginGame
from status import CurrentStatus


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
    begin = BeginGame()
    status = CurrentStatus()
    curr_room = begin.current_player.current_room
    begin.print_beginning()
    status.print_current_status(
        curr_room.name, curr_room.description, curr_room.items)

    command = ''
    while command != 'q':
        command = input('\nEnter a command.\n')
        try:
            if command == 'n':
                new_room = curr_room.n_to
            if command == 'e':
                new_room = curr_room.e_to
            if command == 's':
                new_room = curr_room.s_to
            if command == 'w':
                new_room = curr_room.w_to
            curr_room = new_room
            status.print_current_status(
                curr_room.name, curr_room.description, curr_room.items)
        except:
            print('Bad move!')
    print('Game over!')


if __name__ == "__main__":
    main()
