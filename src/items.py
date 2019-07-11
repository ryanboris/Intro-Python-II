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
room['mountain'].w_to = room['cove']
room['cove'].e_to = room['meadows']
room['cove'].s_to = room['beach']
room['beach'].w_to = room['mines']
room['beach'].n_to = room['aether']
room['mines'].s_to = room['aether']
room['aether'].e_to = room['outside']


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
    ],
    "cove": [
        Item('silvernugget', 'a nugget of silver'), Item(
            'soul', 'you can now cast soul which steals health from enemies'), Item('latern', 'a latern that burns oil')
    ],
    "mountain": [
        Item('oil', 'you can burn this in a latern')

    ],
    "meadows": [
        Item('grass', 'green, green grass'), Item('cow', 'mooooooooo')
    ],

    "aether": [
        Item('darkmatter', '????????'), Item(
            'esper', 'pure energy, oh the power...')
    ],
    "beach": [
        Item('sand', 'it\'s sand')
    ],
    "mines": [
        Item('coal', 'a lump of carbon'), Item('canary', 'a bird in a cage and it is still alive'), Item(
            'stoned', 'a spell that drops a boulder on your enemy')
    ]
}

room['outside'].items = items['outside']
room['foyer'].items = items['foyer']
room['overlook'].items = items['overlook']
room['narrow'].items = items['narrow']
room['treasure'].items = items['treasure']
room['cove'].items = items['cove']
room['mountain'].items = items['mountain']
room['meadows'].items = items['meadows']
room['aether'].items = items['aether']
room['beach'].items = items['beach']
room['mines'].items = items['mines']
