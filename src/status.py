class CurrentStatus:
    def print_current_status(self, room, description, items):
        print(
            f'You are currently located in {room}')
        print(
            f'Description:\n{description}\n')
        print('Room contents:\n')
        for item in items:
            print(item.name)
