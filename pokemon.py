#!/usr/local/bin/python3

import gc
import random
import pkmdatabase as db
import numpy as np  

class Pokemon:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.attack = 50
        self.defence = 50
        self.level = 5
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
    
    #Add 4 attacks to a pokemon. 2 attacks of type "NORMAL" and 2 attacks of its own type.
    def addAttacks(self,dict):
        self.attacks.append(random.choice(dict["NORMAL"]))
        self.attacks.append(random.choice(dict["NORMAL"]))
        self.attacks.append(random.choice(dict[self.type]))
        self.attacks.append(random.choice(dict[self.type]))
             
class Trainer:
    def __init__(self, name):
        self.name = name
        self.team = []

    def selectTeam(self, d):
        keys = random.sample(list(d), 6)
        values = [d[k] for k in keys]
        sample = dict(zip(keys, values))

        _team = []
        for names, types in sample.items():
            _team.append(Pokemon(names, types))
        self.team = _team
         
class PokemonGame:
    def __init__(self, trainers):
        self.player1 = trainers[0]
        self.rivals = trainers[1:]
        self.player2 = trainers[1]
        self.p1_pokedex = self.player1.team
        self.p2_pokedex = self.player2.team
        self.p1_pokemon = None
        self.p2_pokemon = None
        self.turns = 0

    def which_turn(self):
        players = [self.player1, self.player2]
        return players[self.turns % 2]

    #Print player 1 and player 2's Name, current pokemon, and their hp
    def printBattleStatus(self):
        print("-"*70)
        print(self.player2.name + "'s " + self.p2_pokemon.name)
        print("HP: {hp}".format(hp = round((self.p2_pokemon.health/self.p2_pokemon.max_health) * 100)))
        print("\n")
        print(self.player1.name + "'" + self.p1_pokemon.name)
        print("HP: {hp}".format(hp = round((self.p1_pokemon.health/self.p1_pokemon.max_health) * 100)))
        attacks =["("+str(i+1)+") " + self.p1_pokemon.attacks[i].name for i in range(4)]
        print("-"*60)
        print("Fight! Select your next attack, type a number from 1 - 4:")
        print(attacks)
        print("-"*70)
        print("\n")

    def selectAttack(attack = "this key var is just here to fix a bug"):
        validselections = [1,2,3,4]
        attackSelected = False
        while attackSelected == False:
            try:
                selection = int(input())
            except ValueError:
                print("Invalid option! Select again")
                continue
            if selection in validselections:    
                attackSelected == True
                break
            else:
                print("Invalid option! Select again")
        return selection - 1

#Function to iterate through all instances of a class.
def get_all_instances(of_class):
    _instances = []
    for obj in gc.get_objects():
        if isinstance(obj,of_class):
            _instances.append(obj)
    return _instances

#Instantiation of trainers.
player1 = Trainer("Ash")
rival1 = Trainer("Brock")
rival2 = Trainer("Misty")
rival3 = Trainer("Team Rocket's James")
rival4 = Trainer("Team Rocket's Jessie")
all_trainers = get_all_instances(Trainer) 

#Instantiation of all attacks in database file.
all_attacks = get_all_instances(db.Attack)

#Group attacks of the same type into attack_types dictionary.
attack_dict = {}
for i in range(0,len(all_attacks)):
    if all_attacks[i].type not in attack_dict:
        attack_dict[all_attacks[i].type] = [all_attacks[i]]
    else:
        attack_dict[all_attacks[i].type] += [all_attacks[i]]

#Add 6 random pokemon to all trainers.
for trainer in all_trainers:
    trainer.selectTeam(db.pokemon_dict)
    
    #Add attacks to each of the trainer's pokemon.
    for pokemon in trainer.team:
        pokemon.addAttacks(attack_dict)

#Function to print   
def printPokedexes():
    for i in range(0,len(all_trainers)):
        print("{name}s Pokedex:".format(name = all_trainers[i].name))
        
        for j in range(0,len(all_trainers[i].team)):
            print("--{pokName}--".format(pokName = all_trainers[i].team[j].name))
            print("Health = {health}".format(health = all_trainers[i].team[j].health))
            
            for k in range(0,len(all_trainers[i].team[j].attacks)):
                print(" -{attName}: {attType}, {attPower}".format(attName = all_trainers[i].team[j].attacks[k].name, attType = all_trainers[i].team[j].attacks[k].type, attPower = all_trainers[i].team[j].attacks[k].power))
            print("\n")    

#Returns efficacy of an attack
def typeDamageCalc(attackType = "NORMAL", defendingPkmType = "NORMAL"):
    return db.typechart[db.typeindices.index(attackType)][db.typeindices.index(defendingPkmType)]

#Returns the total damage an attack inflicts.
def damage(attackingPkm, defendingPkm, attackIndex):
    total = (((2/5 * attackingPkm.level + 2) * attackingPkm.attacks[attackIndex].power * attackingPkm.attack/attackingPkm.defence) / 50 + 2)
    #total = total * typeDamageCalc(attackingPkm.attack[attackIndex].type), (defendingPkm.type)
    return total
       
def playGame():
    game = PokemonGame(all_trainers)
    gameOver = False

    while gameOver == False:
        game.player2 = game.rivals[0]
        game.p1_pokemon = game.p1_pokedex[0]
        game.p2_pokemon = game.p2_pokedex[0]

        game.printBattleStatus()
        selection = game.selectAttack()
        game.p2_pokemon.decreaseHealth(damage(game.p1_pokemon, game.p2_pokemon, selection))
    
        if game.p2_pokemon.health == 0:
            game.p2_pokedex.pop(0)
        
        if game.p2_pokedex == []:
            game.rivals.pop(0)

        if game.player2 == game.player1:
            gameOver = True


def main():
    playGame()

if __name__ == "__main__":
    main()
