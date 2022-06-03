import gc
import random

class Pokemon:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.attacks = []
        self.health = 120 #or its level * 5
        self.max_health = 120 # or its level * 5
        self.is_knocked_out = False

    #Lower health bar
    def decreaseHealth(self, amount):
        self.health -= amount
        if (self.health <= 0):
            self.health = 0
            self.is_knocked_out = True
            print(f"{self.name} is knocked out.")
    
    def addAttacks(self,attacks):
        self.type = attacks
        
class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = {}
        self.pokemonObjects = []
        self.current_pokemon = 0 

    def selectTeam(self, all_poks):
        team = {}
        for i in range(0, 6):
            pok_names, pok_types = random.choice(list(all_poks.items()))
            team[pok_names] = pok_types
        self.pokemons = team
    
    def createPokemonObjects(self):
        team = []
        for names, types in self.pokemons.items():
            team.append(Pokemon(names, types))
        self.pokemonObjects = team
            
class Attack:
    def __init__(self, name, type, power):
        self.name = name
        self.type = type
        self.power = power

#All pokemons available.
pokemon_dict = {'Charmander': 'FIRE', 'Bulbasaur': 'GRASS', 'Squirtle': 'WATER', 'Pikachu': 'ELECTRIC', 'Geodude': 'ROCK', 'Pidgey': 'FLYING'}

#Instantiation of attacks.
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

#Instantiation of trainers.
trainer1 = Trainer("Brock")
trainer2 = Trainer("Misty")
trainer3 = Trainer("Team Rocket's James")
trainer4 = Trainer("Team Rocket's Jessie")

#Function to iterate through all instances of a class.
def get_all_instances(of_class):
    _instances = []
    for obj in gc.get_objects():
        if isinstance(obj,of_class):
            _instances.append(obj)
    return _instances
all_attacks = get_all_instances(Attack)
all_trainers = get_all_instances(Trainer) 

#Add 6 random Pokemons to all trainers.
for trainer in all_trainers:
    trainer.selectTeam(pokemon_dict)
    trainer.createPokemonObjects()

    #Add attacks to pokemons.
    for i in range(0,6):
        trainer.pokemonObjects[i]

print(trainer3.pokemonObjects[0].type)


