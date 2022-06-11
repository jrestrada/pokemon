import numpy as np  

#All pokemon available.
pokemon_dict = {'Charmander': 'FIRE', 
                'Bulbasaur': 'GRASS',
                'Squirtle': 'WATER',
                'Pikachu': 'ELECTRIC',
                'Geodude': 'ROCK',
                'Pidgey': 'FLYING'}

# Types in order to be used as indices for typechart
typeindices= ["NORMAL","FIRE","WATER","ELECTRIC","GRASS","ICE","FIGHTING",
            "POISON","GROUND","FLYING","PSYCHIC","BUG","ROCK","GHOST","DRAGON"]

# Type indices is just a temporary list of strings to test the code, 

typechart = np.array([[1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,0.5,0  ,1  ],  

                      [1  ,0.5,0.5,1  ,2  ,2  ,1  ,1  ,1  ,1  ,1  ,2  ,0.5,1  ,0.5], 
                      [1  ,2  ,0.5,1  ,0.5,1  ,1  ,1  ,2  ,1  ,1  ,1  ,2  ,1  ,0.5],
                      [1  ,1  ,2  ,0.5,0.5,1  ,1  ,1  ,0  ,2  ,1  ,1  ,1  ,1  ,0.5],
                      [1  ,0.5,2  ,1  ,0.5,1  ,1  ,0.5,2  ,0.5,1  ,0.5,2  ,1  ,0.5],

                      [1  ,1  ,0.5,1  ,2  ,0.5,1  ,1  ,2  ,2  ,1  ,1  ,1  ,1  ,2  ],  
                      [2  ,1  ,1  ,1  ,1  ,2  ,1  ,0.5,1  ,0.5,0.5,0.5,2  ,0  ,1  ],
                      [1  ,1  ,1  ,1  ,2  ,1  ,1  ,0.5,0.5,1  ,1  ,2  ,0.5,0.5,1  ],
                      [1  ,2  ,1  ,2  ,0.5,1  ,1  ,2  ,1  ,0  ,1  ,0.5,2  ,1  ,1  ],  
                      [1  ,1  ,1  ,0.5,2  ,1  ,2  ,1  ,1  ,1  ,1  ,2  ,0.5,1  ,1  ],
                      [1  ,1  ,1  ,1  ,1  ,1  ,2  ,2  ,1  ,1  ,0.5,1  ,1  ,1  ,1  ],
                      [1  ,0.5,1  ,1  ,2  ,1  ,0.5,2  ,1  ,0.5,2  ,1  ,1  ,0.5,1  ],
                      [1  ,2  ,1  ,1  ,1  ,2  ,0.5,1  ,0.5,2  ,1  ,2  ,1  ,1  ,1  ],
                      [0  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,0  ,1  ,1  ,2  ,1  ],
                      [1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,2  ]])

class Attack:
    def __init__(self, name, type, power):
        self.name = name
        self.type = type
        self.power = power

scratch = Attack("Scratch", "NORMAL", 40)
cut = Attack("Cut", "NORMAL", 50)
strength = Attack("Strengh", "NORMAL", 80)
skull_bash = Attack("Skull Bash", "NORMAL",130)
solar_beam = Attack("Solar Beam", "GRASS", 120)
seed_bomb = Attack("Seed Bomb", "GRASS", 80)
thunderbolt = Attack("Thunderbolt", "ELECTRIC", 90)
spark = Attack("Spark", "ELECTRIC", 65)
rock_blast = Attack("Rock Blast", "ROCK", 25)
double_edge = Attack("Double Edge", "ROCK", 120)
flame_thrower = Attack("Flame Thrower", "FIRE", 90)
inferno = Attack("Inferno", "FIRE", 100)
fly = Attack("Fly", "FLYING", 90)
aereal_ace = Attack("Aereal Ace", "FLYING", 60)
surf = Attack("Surf", "WATER", 90)
waterfall = Attack("Waterfall", "WATER", 80)



