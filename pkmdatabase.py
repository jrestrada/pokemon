import numpy as np  

#All pokemon available.
pokemon_dict = {'Bulbasaur':     'GRASS', 
                'Ivysaur':       'GRASS',
                'Venusaur':      'GRASS',
                'Charmander':    'FIRE',
                'Charmeleon':    'FIRE',
                'Charizard':     'FIRE',
                'Squirtle':      'WATER',
                'Wartortle':     'WATER',
                'Blastoise':     'WATER',
                'Caterpie':      'BUG',
                'Metapod':       'BUG',
                'Buterfree':     'BUG',
                'Weedle':        'BUG',
                'Kakuna': 'BUG',
                'Beedril': 'BUG',
                'Pidgey': 'FLYING',
                'Pidgeotto': 'FLYING',
                'Pidgeot': 'FLYING',
                'Rattata': 'NORMAL',
                'Ratticate': 'NORMAL',
                'Spearrow': 'FLYING',
                'Fearrow': 'FLYING',
                'Ekans': 'POISON',
                'Arbok': 'POISON',
                'Pikachu': 'ELECTRIC',
                'Raichu': 'ELECTRIC',
                'Sandshrew': 'GROUND',
                'Sandslash': 'GROUND',
                'Nidoran_f': 'POISON',
                'Nidorina': 'POISON',
                'Nidoqueen': 'POISON',
                'Nidoran_m': 'POISON',
                'Nidorino': 'POISON',
                'Nidoking': 'POISON',
                'Clefairy': 'NORMAL',
                'Clefable': 'NORMAL',
                'Vulpix': 'FIRE',
                'Ninetales': 'FIRE',
                'Jigglypuff': 'NORMAL',
                'Wigglytuff': 'NORMAL',
                'Zubat': 'POISON',
                'Golbat': 'FLYING',
                'Oddish': 'GRASS',
                'Gloom': 'GRASS',
                'Vileplume': 'GRASS',
                'Paras': 'POISON',
                'Parasect': 'POISON',
                'Venonat': 'BUG',
                'Venomoth': 'BUG',
                'Diglett': 'GROUND',
                'Dugtrio': 'GROUND',
                'Meowth': 'NORMAL',
                'Persian': 'NORMAL',
                'Psyduck': 'WATER',
                'Golduck': 'WATER',
                'Mankey': 'FIGHTING',
                'Primeape': 'FIGHTING',
                'Growlithe': 'FIRE',
                'Arcanine': 'FIRE',
                'Poliwag': 'WATER',
                'Poliwhirl': 'WATER',
                'Poliwrath': 'WATER',
                'Abra': 'PSYCHIC',
                'Kadabra': 'PSYCHIC',
                'Alakazam': 'PSYCHIC',
                'Machop': 'FIGHTING',
                'Machoke': 'FIGHTING',
                'Machamp': 'FIGHTING',
                'Bellsprout': 'GRASS',
                'Weepinbell': 'GRASS',
                'Victreebel': 'GRASS',
                'Tentacool': 'POISON',
                'Tentacruel': 'WATER',
                'Geodude': 'ROCK',
                'Graveler': 'ROCK',
                'Golem': 'ROCK',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
                # '': '',
# 
                }

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
    def __init__(self, name, type, power, addedEffect = "eff_none"):
        self.name = name
        self.type = type
        self.power = power
        self.addedEffect = addedEffect

    # def eff_none(self):
        # print("No Added Effect")    
# 
    # def activate_added_effect(self):
        # locals()[self.addedEffect]()




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
acid = Attack("Acid", "POISON", 40)
poison_sting = Attack("Poison Sting", "POISON", 15)
rolling_kick = Attack("Rolling Kick","FIGHTING", 60)
double_kick = Attack("Double Kick","FIGHTING", 30)
psybeam = Attack("Psybeam","PSYCHIC", 65)
psychic = Attack("Psychic","PSYCHIC", 90)
dig = Attack("Dig", "GROUND", 80)
earthquake = Attack("Earthquake", "GROUND", 100)
leech_life = Attack("Leech Life", "BUG", 80)
Pin_Missile = Attack("Earthquake", "BUG", 25)






