# Making a hero
class Hero:
    def __init__(self, name, health, damage, gender, path, weapon_name, affinity):
        self.level = 1
        self.exp = None
        self.name = name
        self.path = path
        self.health = health
        self.damage = damage
        self.weapon_name = weapon_name
        self.gender = gender
        self.sockets = []
        self.affinity = affinity
        
    def __str__(self):
        return f"""
Hero Name: {self.name}
Hero Class: {self.path}
Hero Damage: {self.damage}
Gender: {self.gender}
Weapon: {self.weapon_name}
Hit Points: {self.health}
Hero Level: {self.level}
Infusion: {self.affinity}
Runes: {self.sockets}
"""
    
    def add_exp(self, e=1):
        self.exp += 100 * e
    

    def level_up(self):
        if self.exp == 1000:
            self.level += 1
            if self.level == 2 and self.path == "DPS":
                self.damage += 15
                self.health += 10
            elif self.level == 2 and self.path == "Tank":
                self.damage += 10
                self.health += 15
            elif self.level == 2 and self.path == "Ranger":
                self.damage += 15
                self.health += 5
            else:
                self.damage += 10
                self.health += 10
        elif self.exp == 1750:
            self.level += 1
            if self.level == 3 and self.path == "DPS":
                self.damage += 15
                self.health += 10
            elif self.level == 3 and self.path == "Tank":
                self.damage += 10
                self.health += 15
            elif self.level == 3 and self.path == "Ranger":
                self.damage += 15
                self.health += 5
            else:
                self.damage += 10
                self.health += 10
        elif self.exp == 2500:
            self.level += 1
            if self.level == 4 and self.path == "DPS":
                self.damage += 15
                self.health += 10
            elif self.level == 4 and self.path == "Tank":
                self.damage += 10
                self.health += 15
            elif self.level == 4 and self.path == "Ranger":
                self.damage += 15
                self.health += 5
            else:
                self.damage += 10
                self.health += 10
        elif self.exp == 4000:
            self.level += 1
            if self.level == 5 and self.path == "DPS":
                self.damage += 15
                self.health += 10
            elif self.level == 5 and self.path == "Tank":
                self.damage += 10
                self.health += 15
            elif self.level == 5 and self.path == "Ranger":
                self.damage += 15
                self.health += 5
            else:
                self.damage += 10
                self.health += 10
            

    def base_attack(self, other):
        other.recieve_damage(self.damage) 
        
    def recieve_damage(self, damage):
        if "Def Bonus" in self.runes:
            self.health -= (0.8*damage)
        self.health -= damage    

    def add_runes(self, other):
        import random
        import json
        runes = ['Exp Bonus', 'HP Bonus', 'Element Damage Bonus', 'Attack Bonus', 'Def Bonus']
        
        if len(self.sockets) >= 3:
            return "All sockets full"
        else:
            rune = ''
            while rune in self.sockets or rune == '':
                rune = random.choice(runes)
            self.sockets.append(rune)
            if rune == 'Attack Bonus':
                self.damage += 20
            elif rune == 'HP Bonus':
                self.health += 20
                    
        with open("storage.json", "r") as f:
            data = json.load(f)
        data[self.name]["runes"].append(rune)
        with open("storage.json", "w") as f:
            json.dump(data, f, indent=4)
        
        
        return f'Rune ({rune}) Obtained.'
    
    def _update(self):
        import json
        with open("storage.json", "r") as f:
            data = json.load(f)
        data.update({self.name: {
            "health": 1000,
            "damage": 100,
            "weapon": self.weapon_name,
            "gender": self.gender,
            "runes": self.sockets,
            "affinity": self.affinity
        }})
        with open("storage.json", 'w') as file:
            json.dump(data, file, indent=4)

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.deck = []
        
    def play(self, card):
        self.hand.remove(card)
        


# Game Start

def game_start():
    up_time = True
    turn = 0
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    while up_time == True:
        if turn == 8:
            up_time = False
        turn += 1

# pose = Hero("Hungirv", "Male", "Tupnir's edge", "Chaos")
# pose._update()

# pose1 = Hero("Terissa", "Female", "Ragnorock", "Earth")
# pose1._update()
