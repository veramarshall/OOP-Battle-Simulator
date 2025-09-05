from enemy import enemy

class baby_elf(enemy):
    #new ability
    def cry():
        print("wah wahh")

#overriding take dammage
    def take_damage(self, damage):
        print("this is a baby dont hurt it")
        return super().take_damage(damage)