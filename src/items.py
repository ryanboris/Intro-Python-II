from rooms import room
from item import Item

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


items = {
    "outside": [
        Item('wand', 'a magic wand of many wonders'),
        Item('staff', 'the staff of one thousand truths')
    ],
    "foyer": [
        Item('cardboard', 'a pretty crappy item, at least it appears to be.')
    ],
    "overlook": [
        Item('mana', 'a bottle of mana'),
        Item('fire', 'a basic fire spell'),
        Item('ice', 'a basic, but cool ice spell')
    ],
    "narrow": [
        Item('potion', 'a bottle of an odd, unknown viscous material'),
        Item('luck', 'the fairy Queen casts the spell of Luck upon yee soul.')
    ],
    "treasure": [
        Item('goldnugget', 'A gold nugget, pretty self-explanatory'),
        Item('doom', 'this pretty much just blows up the entire world except for parts of Antartica, and half of Sri Lanka.')
    ]
}

room['outside'].items = items['outside']
room['foyer'].items = items['foyer']
room['overlook'].items = items['overlook']
room['narrow'].items = items['narrow']
room['treasure'].items = items['treasure']

