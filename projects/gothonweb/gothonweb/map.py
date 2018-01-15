# -*-coding:utf-8-*-
class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
        
    def go(self, direction):
        return self.paths.get(direction, None)
        
    def add_paths(self, paths):
        self.paths.update(paths)
        
central_corridor = Room("Central Corridor",
"""
The Gothon of Planet Percal #25 have invaded your ship. You are the last surviving member 
and you have to escape here. But you meet a Gothon, you have to choose what to do.
""")

laser_weapon_armory = Room("Laser Weapon Armory",
"""
You do a dive roll into the Weapon Armory. There is a keypad lock on the box and you need 
the code to get the bomb out and you have 10 times to try.
""")

the_bridge = Room("The Bridge", 
"""
You run as fast as you can to the bridge where you must place it in the right spot.
""")

escape_pod = Room("Escape Pod", 
"""
There is 5 pods, which one do you take?
""")

the_end_winner = Room("The End", 
"""
You jump into pod 2 and hit the eject button. You won!
""")

the_end_loser = Room("The End", 
"""
You jump into a random pod but it's out of control.
""")

generic_death = Room("death", "You died.")

escape_pod.add_paths({
    '2': the_end_winner,
    '*': the_end_loser                                 # '*'用来实现"捕获所有操作"的功能。
})

the_bridge.add_paths({
    'throw the bomb': generic_death,
    'slowly place the bomb': escape_pod
})

laser_weapon_armory.add_paths({
    '0132': the_bridge,
    '*': generic_death
})

central_corridor.add_paths({
    'shoot!': generic_death,
    'dodge!': generic_death,
    'tell a joke': laser_weapon_armory
})

START = central_corridor