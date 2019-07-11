class Monster:
    def __init__(self, name, description, hp):
        self.name = name
        self.description = description
        self.hp = hp

    def daze(self):
        print(f'{self.name} has cast daze.  Things are feelin pretty strange man...')

    def heal(self):
        self.hp + 100

    def mega_heal(self):
        self.hp + 500

    def attack(self):
        print(f'{self.name} attacks!')
