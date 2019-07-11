# Python crap

```py

welcome_msg = Fancytext("Welcome\nAdventure\nSeeker!", 'gothic')

welcome_msg.print_text()

player_name = input('Please enter your name!\n')

new_player = Player(player_name, room['outside'])

print(
    f'Welcome, {new_player.name}!\nYour journey begins!\n')

user_input = ''

while not user_input == 'q':
    line = Fancytext('-----', 'funky_dr')
    line.print_text()
    print(
        f'You are currently located in {new_player.current_room.name}.\n')

    print(

        f'Description:\n{new_player.current_room.description}\n'
    )

    current_room_items = new_player.current_room.items

    print('Current room items:')
    for item in current_room_items:
        print(item.name)

    user_input = input('\nEnter a command.\n')

    split_input = user_input.split(' ')

    if split_input[0] == 'get' or split_input[0] == 'take':
        room_items = new_player.current_room.items
        for item in room_items:
            if item.name == split_input[1]:
                new_player.current_room.items.remove(item)
                new_player.items.append(item)
                item.on_take()

    if split_input[0] == 'drop':
        for item in new_player.items:
            if item.name == split_input[1]:
                new_player.items.remove(item)
                new_player.current_room.items.append(item)
                item.on_drop()

    if user_input == 'n' or user_input == 'e' or user_input == 'w' or user_input == 's':
        try:
            if user_input == 'n':
                new_room = new_player.current_room.n_to
            if user_input == 'e':
                new_room = new_player.current_room.e_to
            if user_input == 's':
                new_room = new_player.current_room.s_to
            if user_input == 'w':
                new_room = new_player.current_room.w_to
            print(f'You entered the valid move - {user_input}!\n')
            new_player.current_room = new_room

        except:
            print('Move was not valid for current location.\n Try again.\n')
    elif user_input == 'inventory' or user_input == 'i':
        print('This is your current inventory:\n')
        for item in new_player.items:
            print(item.name)
    elif user_input == 'help':
        print('\nEnter n, e, w, s to move to a new room.\nPick up items by using take `item name` or get `item name`\nDrop an item with drop `item name`.\n')


print(pyfiglet.figlet_format('The game has ended!'))

```
