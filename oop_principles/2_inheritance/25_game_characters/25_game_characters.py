
class Character:
    def __init__(self, name):
        self.name       = name
        self.health     = 100
        self.max_health = 100
        self.level      = 1
        self.experience = 0

    def attack(self):
        return 10

    def defend(self, damage):
        return damage

    def take_damage(self, damage):
        actual_damage = self.defend(damage)
        self.health   = self.health - actual_damage
        if self.health < 0:
            self.health = 0

    def heal(self, amount):
        self.health = self.health + amount
        if self.health > self.max_health:
            self.health = self.max_health

    def gain_experience(self, exp):
        self.experience = self.experience + exp
        if self.experience >= 100:
            self.level_up()
            self.experience = 0

    def level_up(self):
        self.level      = self.level + 1
        self.health     = self.max_health
        print(f"{self.name} leveled up to level {self.level}!")

    def is_alive(self):
        return self.health > 0

    def get_status(self):
        status = "Alive" if self.is_alive() else "Dead"
        return f"{self.name} - Level {self.level}\nHealth: {self.health}/{self.max_health}\nStatus: {status}"



class Warrior(Character):
    def __init__(self, name):
        super().__init__(name)
        self.armor  = 10
        self.weapon = "Steel Sword"

    def attack(self):
        return 25 + (self.level * 2)

    def defend(self, damage):
        return damage - self.armor      # armor blocks some damage

    def level_up(self):
        super().level_up()
        self.armor      = self.armor + 5
        self.max_health = self.max_health + 10
        self.health     = self.max_health

    def get_status(self):
        status = "Alive" if self.is_alive() else "Dead"
        return (
            f"Warrior {self.name} - Level {self.level}\n"
            f"Health: {self.health}/{self.max_health}, Armor: {self.armor}, Weapon: {self.weapon}\n"
            f"Status: {status}"
        )



class Mage(Character):
    def __init__(self, name):
        super().__init__(name)
        self.mana     = 50
        self.max_mana = 50
        self.spells   = ["Magic Missile"]

    def attack(self):
        if self.mana >= 10:
            self.mana = self.mana - 10
            return 30 + (self.level * 3)
        return 5

    def defend(self, damage):
        return int(damage * 0.8)

    def level_up(self):
        super().level_up()
        self.max_mana = self.max_mana + 10
        self.mana     = self.max_mana
        self.spells.append("Fireball")

    def cast_spell(self, spell_name):
        if spell_name in self.spells and self.mana >= 10:
            self.mana = self.mana - 10
            print(f"{self.name} casts {spell_name}!")
        else:
            print(f"{self.name} cannot cast {spell_name}!")

    def get_status(self):
        status = "Alive" if self.is_alive() else "Dead"
        return (
            f"Mage {self.name} - Level {self.level}\n"
            f"Health: {self.health}/{self.max_health}, Mana: {self.mana}/{self.max_mana}\n"
            f"Spells: {self.spells}\n"
            f"Status: {status}"
        )



class Archer(Character):
    def __init__(self, name):
        super().__init__(name)
        self.arrows   = 30
        self.bow_type = "Longbow"
        self.accuracy = 0.85

    def attack(self):
        if self.arrows > 0:
            self.arrows = self.arrows - 1
            return int(20 + (self.level * 2.5))
        return 5

    def defend(self, damage):
        return int(damage * 0.9)

    def level_up(self):
        super().level_up()
        self.accuracy = self.accuracy + 0.05
        self.arrows   = self.arrows + 10

    def reload_arrows(self, count):
        self.arrows = self.arrows + count
        print(f"{self.name} reloaded {count} arrows!")

    def get_status(self):
        status = "Alive" if self.is_alive() else "Dead"
        return (
            f"Archer {self.name} - Level {self.level}\n"
            f"Health: {self.health}/{self.max_health}, Arrows: {self.arrows}, Bow: {self.bow_type}\n"
            f"Accuracy: {int(self.accuracy * 100)}%\n"
            f"Status: {status}"
        )



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
