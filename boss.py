from enemy import enemy 
import random


class evilLion(enemy):
    def __init__(self,name):
        super().__init__(name)
        self.health = 1000
        self.attack_power = 10

    def throwup(self):
        chance = random.randint(1,10)
        if chance > 8:
            print("blehhhh")

    def bite(self):
        if self.health < 20 and self.health > 0:
            self.attack_power = self.attack_power + 10
        return self.attack_power
