# Making a hero

class Hero:
    def __init__(self, name, gender, weapon_name, affinity):
        self.level = 0
        self.health = 100
        self.damage = 100
        self.weapon_name = weapon_name
        self.gender = gender
        self.sockets = []
        self.affinity = affinity
        self.name = name
        
    def __str__(self):
        return f"""
Hero Name: {self.name}
Durability: {self.gender}
Weapon Type: {self.weapon_name}
Hit Points: {self.health}
Hero Level: {self.level}
Infusion: {self.affinity}
Runes: {self.sockets}
"""
    
    def add_runes(self):
        import random
        import json
        runes = ['Dmg Bonus', 'HP Bonus', 'Element Damage', 'Speed Bonus', 'Def Bonus']
        
        if len(self.sockets) >= 3:
            return "All sockets full"
        else:
            rune = ''
            while rune in self.sockets or rune == '':
                rune = random.choice(runes)
            self.sockets.append(rune)
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
            "health": 100,
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

pose = Hero("Hungirv", "Male", "Tupnir's edge", "Chaos")
pose._update()
pose.add_runes()
pose.add_runes()
pose.add_runes()
pose1 = Hero("Terissa", "Female", "Ragnorock", "Earth")
pose1._update()
pose1.add_runes()
pose1.add_runes()
pose1.add_runes()
