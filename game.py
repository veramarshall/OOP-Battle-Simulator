import random
from goblin import Goblin
from hero import Hero
from boss import evilLion

def main():
    print("Welcome to the Battle Arena!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")

    # Create a hero
    hero = Hero("Aragorn")

    # Create goblins ༼ ºل͟º ༽ ༼ ºل͟º ༽ ༼ ºل͟º ༽
    goblins = [Goblin(f"Goblin {i+1}", "green") for i in range(5)]

    # Keep track of how many goblins were defeated
    defeated_goblins = 0
    total_damage = 0
    rounds = 0

    # Battle Loop 
    while hero.is_alive() and any(goblin.is_alive() for goblin in goblins):
        print("\nNew Round!")
        rounds = rounds + 1
        # Hero's turn to attack
        target_goblin = random.choice([goblin for goblin in goblins if goblin.is_alive()])
        damage = hero.strike()
        print(f"Hero attacks {target_goblin.name} for {damage} damage!")
        target_goblin.take_damage(damage)

        # Check if the target goblin was defeated
        if not target_goblin.is_alive():
            defeated_goblins += 1
            print(f"{target_goblin.name} has been defeated!")

        # Goblins' turn to attack
        for goblin in goblins:
            if goblin.is_alive():
                damage = goblin.attack()
                print(f"{goblin.name} attacks hero for {damage} damage!")
                hero.receive_damage(damage)
            total_damage = total_damage + damage

    # Determine outcome
    if hero.is_alive():
        print(f"\nThe hero has defeated all the goblins! ༼ ᕤ◕◡◕ ༽ᕤ")
    else:
        print(f"\nThe hero has been defeated. Game Over. (｡•́︿•̀｡)")

    if hero.is_alive():
        print("oh no BOSS EVIL LION -----------------------------------------------------")
        lion = evilLion("evil Lion")
        while hero.is_alive() and lion.is_alive:
            damage = hero.strike()
            lion.take_damage(damage)
            damage = lion.attack()
            hero.receive_damage(damage)
        if hero.is_alive():
            print("\nhero defeated the evil lion")
        else:
            print("\nhero is dead..")


    # Final tally of goblins defeated
    print(f"\nTotal goblins defeated: {defeated_goblins} / {len(goblins)}")
    print(f"\ntotal damage taken: {total_damage}")
    print(f"\nrounds survived: {rounds}")


if __name__ == "__main__":
    main()
