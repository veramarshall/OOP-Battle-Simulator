import random
from enemy import enemy
class Goblin(enemy):
    """
    This is our goblin blueprint 
    
    Attributes:
        name: Awe, it has a name? How cute!
        health: The current health value 
        attack_power: How much health will be drained from opponent if hit
    """
    def __init__(self, name, color):
        super().__init__(name)
        self.health = 50
        self.color = color
        
    