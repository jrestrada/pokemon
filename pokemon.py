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
        self.attacks = attacks
        
class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = {}
        self.current_pokemon = 0 

    def selectTeam(self, all_poks):
        team = {}
        for i in range(6):
            pok_names, pok_types = random.choice(list(all_poks.items()))
            team[pok_names] = pok_types
        self.pokemons = team

    def assemble_team(self, pokemons):
        team = []
        random_indices = random.sample(range(len(pokemons)), 6)
        for i in random_indices:
            team.append(pokemons[i])
        self.pokemons = team
        
class Attack:
    def __init__(self, name, type, power):
        self.name = name
        self.type = type
        self.power = power

#Instantiation of pokemons.
charmander = Pokemon("Charmander", "FIRE")
bulbasaur = Pokemon("Bulbasaur", "GRASS")
squirtle = Pokemon("Squirtle", "WATER")
pikachu = Pokemon("Pikachu", "ELECTRIC")
geodude = Pokemon("Geodude", "ROCK")
pidgey = Pokemon("Pidgey", "FLYING")

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
trainer2 = Trainer("Team Rocket's James")
trainer2 = Trainer("Team Rocket's Jessie")

#Function to iterate through all instances of a class.
def get_all_instances(of_class):
    _instances = []
    for obj in gc.get_objects():
        if isinstance(obj,of_class):
            _instances.append(obj)
    return _instances
all_attacks = get_all_instances(Attack)

#Add 6 random Pokemon objects to the pokemons atribute of the trainer object.
#trainer1.assemble_team(all_pokemon)




#create a copy of each pokemon when added to a trainer so that repetition of pokemons is possible.

pokemon_dict = {'Charmander': 'FIRE', 'Bulbasaur': 'GRASS', 'Squirtle': 'WATER', 'Pikachu': 'ELECTRIC', 'Geodude': 'ROCK', 'Pidgey': 'FLYING'}

trainer1.selectTeam(pokemon_dict)
print(trainer1.pokemons)


#for i in trainer1_pokemons:
    #trainer1_pokemons[i].createPokemon()

