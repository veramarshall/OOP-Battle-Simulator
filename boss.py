from enemy import enemy 

class evilLion(enemy):
    def throwup():
        print("blehhhh")

    def __init__(self):
        self.health = 1000
        self.attack_power = 1000
    
    def bite(self):
        if self.health < 100:
            self.attack_power = self.attack_power + 100
        return self.attack_power
