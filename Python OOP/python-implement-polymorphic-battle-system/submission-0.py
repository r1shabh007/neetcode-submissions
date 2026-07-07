class Hero:
    def __init__(self, name: str, power: int):
        self.name = name
        self.health = 100
        self.power = power
    
    def attack(self) -> int:
        return self.power

# TODO: Implement the Warrior and Mage classes

class Warrior(Hero):
    def __init__(self, name: str, power: int):
        super().__init__(name, power)
        self.power = power + 10

class Mage(Hero):
    def __init__(self, name: str, power: int):
        super().__init__(name, power)
        self.health = 80
        self.power = power + 20

# TODO: Implement the battle function
def show_attack(character) -> None:
    print(f"{character.name} attacks with {character.attack()} damage!")

# Do not modify the following code
warrior = Warrior("Bob", 20)
mage = Mage("Alice", 15)

show_attack(warrior)  
show_attack(mage)    
