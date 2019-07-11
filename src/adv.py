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
    curr_player = begin.current_player
    curr_room = begin.current_player.current_room
    begin.print_beginning()
    status.print_current_status(
        curr_room.name, curr_room.description, curr_room.items)

    command = ''
    while command != 'q':
        command = input('\nEnter a command.\n')
        split_cmd = command.split(' ')

        if len(split_cmd) == 2:
            if split_cmd[0] == 'get' or split_cmd[0] == 'take':
                for item in curr_room.items:
                    if item.name == split_cmd[1]:
                        curr_room.items.remove(item)
                        curr_player.items.append(item)
                        item.on_take()
                        print('Your current items\n')
                        for item in curr_player.items:
                            print(item.name)
                        print('Room inventory:\n')
                        for item in curr_room.items:
                            print(item.name)

            if split_cmd[0] == 'drop':
                for item in curr_player.items:
                    if item.name == split_cmd[1]:
                        curr_player.items.remove(item)
                        curr_room.items.append(item)
                        item.on_drop()
                        print('Your current items\n')
                        for item in curr_player.items:
                            print(item.name)
                        print('Room inventory:\n')
                        for item in curr_room.items:
                            print(item.name)

        elif command == 'inventory':
            print('Current items:\n')
            for item in curr_player.items:
                print(item.name)

        elif command == 'status':
            status.print_current_status(
                curr_room.name, curr_room.description, curr_room.items)
        elif command == 'n' or command == 'e' or command == 'w' or command == 's':
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
        elif command == 'q':
            print('Game over!')
            break
        else:
            print('Illegal command.')


if __name__ == "__main__":
    main()
