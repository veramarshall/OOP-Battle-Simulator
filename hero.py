import random
class Hero:
    """
    This is our hero blueprint.
    
    O=('-'Q)

    Attributes:
        name: The name of our adventurer.
        hp: The current health value.
        strength: The amount of damage the hero can deal.
        (Bonus) defence: A hero's ability to reduce incoming damage.
        (Bonus) special_ability: A unique ability the hero can use.
    """
    
    def __init__(self, name):
        self.name = "wow"
        self.health = 10000
        self.attack_power = random.randint(10, 100)
    

    def strike(self):
        return random.randint(10, self.attack_power)
        
    def receive_damage(self, damage):
        self.health= self.health - damage
        if self.health < 0:
            print("hero health is 0")
            self.health = 0
        print(f"{self.name} takes {damage} damage. Health is {self.health}.")
    
    def is_alive(self):
        return self.health > 0
    
