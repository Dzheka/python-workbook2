class Character:
    def __init__(self, name):
        self.name = name
        self.max_health = 100
        self.health = 100
        self.level = 1
        self.experience = 0

    def attack(self):
        return 10

    def defend(self, damage):
        return damage

    def take_damage(self, damage):
        actual = self.defend(damage)
        self.health = max(0, self.health - actual)

    def heal(self, amount):
        self.health = min(self.max_health, self.health + amount)

    def gain_experience(self, exp):
        self.experience += exp
        if self.experience >= 100:
            self.level_up()
            self.experience -= 100

    def level_up(self):
        self.level += 1
        self.health = self.max_health

    def is_alive(self):
        return self.health > 0

    def get_status(self):
        return f"{self.name} - Level {self.level}\nHealth: {self.health}/{self.max_health}\nStatus: {'Alive' if self.is_alive() else 'Dead'}"


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name)
        self.armor = 10
        self.weapon = "Steel Sword"

    def attack(self):
        return 25 + (self.level * 2)

    def defend(self, damage):
        return max(0, damage - self.armor)

    def level_up(self):
        self.armor += 5
        self.max_health += 10
        self.health = self.max_health
        self.level += 1

    def get_status(self):
        return f"Warrior {self.name} - Level {self.level}\nHealth: {self.health}/{self.max_health}, Armor: {self.armor}, Weapon: {self.weapon}\nStatus: {'Alive' if self.is_alive() else 'Dead'}"


class Mage(Character):
    def __init__(self, name):
        super().__init__(name)
        self.max_mana = 50
        self.mana = 50
        self.spells = ["Magic Missile"]

    def attack(self):
        if self.mana >= 10:
            self.mana -= 10
            return 30 + (self.level * 3)
        return 5

    def defend(self, damage):
        return int(damage * 0.8)

    def level_up(self):
        self.max_mana += 10
        self.mana = self.max_mana
        self.spells.append("Fireball")
        self.health = self.max_health
        self.level += 1

    def cast_spell(self, spell_name):
        if self.mana >= 10:
            self.mana -= 10
            print(f"{self.name} casts {spell_name}!")
        else:
            print("Not enough mana!")

    def get_status(self):
        return f"Mage {self.name} - Level {self.level}\nHealth: {self.health}/{self.max_health}, Mana: {self.mana}/{self.max_mana}\nSpells: {self.spells}\nStatus: {'Alive' if self.is_alive() else 'Dead'}"


class Archer(Character):
    def __init__(self, name):
        super().__init__(name)
        self.arrows = 30
        self.bow_type = "Longbow"
        self.accuracy = 0.85

    def attack(self):
        if self.arrows > 0:
            self.arrows -= 1
            return 20 + (self.level * 2.5)
        return 5

    def defend(self, damage):
        return int(damage * 0.9)

    def level_up(self):
        self.accuracy += 0.05
        self.arrows += 10
        self.health = self.max_health
        self.level += 1

    def reload_arrows(self, count):
        self.arrows += count

    def get_status(self):
        return f"Archer {self.name} - Level {self.level}\nHealth: {self.health}/{self.max_health}, Arrows: {self.arrows}, Bow: {self.bow_type}\nAccuracy: {int(self.accuracy * 100)}%\nStatus: {'Alive' if self.is_alive() else 'Dead'}"

warrior = Warrior("Conan")
mage    = Mage("Gandalf")
archer  = Archer("Legolas")

print(warrior.get_status())
print()
print(mage.get_status())
print()
print(archer.get_status())

print(f"\n{warrior.name} attacks for {warrior.attack()} damage!")
print(f"{mage.name} attacks for {mage.attack()} damage!")
print(f"{archer.name} attacks for {archer.attack()} damage!")

warrior.take_damage(15)
mage.take_damage(20)
archer.take_damage(12)

warrior.gain_experience(100)
mage.gain_experience(150)
archer.gain_experience(120)

print("\nAfter combat:")
print(warrior.get_status())
print()
print(mage.get_status())
print()
print(archer.get_status())
