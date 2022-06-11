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

    def selectTeam(self, d, n):
        keys = random.sample(list(d), n)
        values = [d[k] for k in keys]
        sample = dict(zip(keys, values))
        _team = []
        for names, types in sample.items():
            _team.append(Pokemon(names, types))
        self.team = _team
         
class PokemonGame:
    def __init__(self, trainers):
        self.player = trainers[0]
        self.rivals = trainers[1:]
        self.rival = self.rivals[0]
        # self.p1_team = self.player.team   these lines are redundant. game already has player. player already has team. game can always access player.team
        # self.p2_team = self.rival.team   these lines are redundant. game already has player. player already has team. game can always access player.team
        self.player_pkm = None
        self.rival_pkm = None
        self.turns = 0

    def which_turn(self):
        players = [self.player, self.rival]
        return players[self.turns % 2]

    # Obtains and returns user selection for player attack and a random selection for Rival Attack
    def selectAttacks(attack = "this key var is just here to fix a bug"):
        validselections = [1,2,3,4]
        rivalSelection = random.sample(validselections, 1)
        attackSelected = False
        while attackSelected == False:
            try:
                playerSelection = int(input())
            except ValueError:
                print("Invalid option! Select again")
                continue
            if playerSelection in validselections:    
                attackSelected == True
                break
            else:
                print("Invalid option! Select again")
        return playerSelection - 1 , rivalSelection[0] - 1

    #Print player 1 and player 2's Name, current pokemon, and their hp
    def printBattleStatus(self):
        print("-"*70)
        print(self.rival.name + "'s " + self.rival_pkm.name)
        print("HP: {hp}".format(hp = round((self.rival_pkm.health/self.rival_pkm.max_health) * 100)))
        print("\n")
        print(self.player.name + "'" + self.player_pkm.name)
        print("HP: {hp}".format(hp = round((self.player_pkm.health/self.player_pkm.max_health) * 100)))
        attacks =["("+str(i+1)+") " + self.player_pkm.attacks[i].name for i in range(4)]
        print("-"*60)
        print("Fight! Select your next attack, type a number from 1 - 4:")
        print(attacks)
        print("-"*70)
        print("\n")


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

#Add n random pokemon to all trainers.
for trainer in all_trainers:
    trainer.selectTeam(db.pokemon_dict, 1)
    
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
def typeDamageMultiplier(attackType = "NORMAL", defendingPkmType = "NORMAL"):
    return db.typechart[db.typeindices.index(attackType)][db.typeindices.index(defendingPkmType)]

def stabDamageMultiplier(attackType = "NORMAL", attackingPkmType = "NORMAL"):
    if attackType == attackingPkmType:
        return 2
    else:
        return 1

#Returns the total damage an attack inflicts.
def damage(attackingPkm, defendingPkm, attackIndex):
    baseDamage = (((2/5 * attackingPkm.level + 2) * attackingPkm.attacks[attackIndex].power * attackingPkm.attack/attackingPkm.defence) / 50 + 2)
    stabDamage = stabDamageMultiplier(attackingPkm.attacks[attackIndex].type, attackingPkm.type)
    typeDamage = typeDamageMultiplier(attackingPkm.attacks[attackIndex].type, defendingPkm.type)
    if typeDamage == 2:
        print("It's super effective")
    elif typeDamage == 0.5:
        print("It's not very effective")
    elif typeDamage == 0:
        print("It had no effect")
    totalDamage = baseDamage * stabDamage * typeDamage 
    return totalDamage
       
def playGame():
    game = PokemonGame(all_trainers)
    gameOver = False

    while gameOver == False:
        game.rival = game.rivals[0]
        game.player_pkm = game.player.team[0]
        game.rival_pkm = game.rival.team[0]

        game.printBattleStatus()
        playerAttackNum, rivalAttackNum = game.selectAttacks()
        game.rival_pkm.decreaseHealth(damage(game.player_pkm, game.rival_pkm, playerAttackNum))
        # game.player_pkm.decreaseHealth(damage(game.game.rival_pkm,game.player_pkm, rivalAttackNum)) # removed for now, player would lose too fast

        if game.rival_pkm.health == 0:
            game.rival.team.pop(0)    

        if not game.rival.team:
            game.rivals.pop(0)

        if not game.player.team:
            print("You are out of Pokemon")
            gameover = True

        if not game.rivals:
            print("You won!!!")
            gameOver = True            
            
    print("Game Over! exiting game...")


def main():
    playGame()

if __name__ == "__main__":
    main()
