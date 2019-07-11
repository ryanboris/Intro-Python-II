# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def print_current_room_items(self):
        print('Current room items:\n')
        for item in self.current_room.items:
            print(item.name)
