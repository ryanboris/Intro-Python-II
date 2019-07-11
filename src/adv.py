from fancytext import Fancytext
from item import Item
from items import items
from room import Room
from rooms import room as room
from player import Player
from puzzle import Puzzle
from beginning import BeginGame
from status import CurrentStatus
from strings import strings
from monsters import Monster
from fonts import fonts
import random
import threading


def main():
    begin = BeginGame()
    status = CurrentStatus()

    curr_player = begin.current_player
    curr_room = begin.current_player.current_room

    begin.print_beginning()

    status.print_current_status(
        curr_room.name, curr_room.description, curr_room.items)

    command = ''

    count = 0

    # def create_monster():
    #     return Monster('Gelgrox', 'Pure evil energy', 100)

    # def set_interval(func, sec):
    #     def func_wrapper():
    #         set_interval(func, sec)
    #         new_monster = func()
    #         print(f'{new_monster.name} attacks!')
    #     t = threading.Timer(sec, func_wrapper)
    #     t.start()
    #     return t
    # set_interval(create_monster, 500)

    while command != 'q':
        command = input('\nEnter a command.\n')
        if (count % 7 == 0):
            print(
                'You must solve this puzzle to continue.  Fail it and the game is over.')
            random.shuffle(strings)
            random.shuffle(fonts)
            puzzle = Puzzle(strings[0], fonts[0]).shuffle()
            response = input()
            if response == strings[0]:
                print('Good work, carry on\n')
            else:
                print('Game is over better luck next time...')
                break

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
                count += 1
            except:
                print('Bad move!')

        elif command == 'q':
            print('Game over!')
            break

        else:
            print('Illegal command.')


if __name__ == "__main__":
    main()
