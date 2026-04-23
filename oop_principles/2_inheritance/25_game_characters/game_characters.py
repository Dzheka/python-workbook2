class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.max_health = 100
        self.level = 1
        self.experience = 0

    def attack(self):
        return self.attack
    
    def defend(self, damage):
        return
    
    def take_damage(self, damage):
        reduced = self.defend(damage)
        self.health -= reduced
        if self.health < 0:
            self.health = 0
    
    def heal(self, amount):
        self.health = min(self.max_health, self.health + amount)
    
    def gain_experience(self, exp):
        self.experience += exp
        if self.experience >= 100:
            self.experience -= 100
            self.level_up()
    
    def level_up(self):
        self.level += 1
        self.health = self.max_health
    
    def is_alive(self):
        return self.health > 0
    
    def get_status(self):
        return f"{self.__class__.__name__} {self.name} - Level {self.level}\nHealth: {self.health}/{self.max_health}\nStatus: {'Alive' if self.is_alive() else 'Dead'}"
    
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
        super().level_up()
        self.armor += 5
        self.max_health += 10
        self.health = self.max_health
    
class Mage(Character):
    def __init__(self, name):
        super().__init__(name)
        self.mana = 50
        self.max_mana = 50
        self.spells = ["Magic Missile"]

    def attack(self):
        if self.mana >= 10:
            self.mana -= 10
            return 30 + (self.level * 3)
        return 0
    
    def defend(self, damage):
        return int(damage * 0.8)
        
    def level_up(self):
        super().level_up()
        self.max_mana += 10
        self.mana = self.max_mana
        if self.level == 2:
            self.spells.append("Fireball")
    
    def cast_spell(self, spell_name):
        if spell_name in self.spells and self.mana >= 10:
            self.mana -= 10
            return f"{self.name} casts {spell_name}!"
        return f"{self.name} cannot cast {spell_name}"
    
class Archer(Character):
    def __init__(self, name):
        super().__init__(name)
        self.arrows = 30
        self.bow_type = "Longbow"
        self.accuracy = 0.85

    def attack(self):
        if self.arrows > 0:
            self.arrows -= 1
            return int(20 + (self.level * 2.5))
        return 0
    
    def defend(self, damage):
        return int(damage * 0.9)
        
    def level_up(self):
        super().level_up()
        self.accuracy = min(1.0, self.accuracy * 0.05)
        self.arrows += 10
    
    def reload_arrows(self, count):
        self.arrows += count
    
# Create characters
warrior = Warrior("Conan")
mage = Mage("Gandalf")
archer = Archer("Legolas")

# Display initial status
print(warrior.get_status())
print(mage.get_status())
print(archer.get_status())

# Combat simulation
print(f"\n{warrior.name} attacks for {warrior.attack()} damage!")
print(f"{mage.name} attacks for {mage.attack()} damage!")
print(f"{archer.name} attacks for {archer.attack()} damage!")

# Take damage
warrior.take_damage(15)
mage.take_damage(20)
archer.take_damage(12)

# Gain experience and level up
warrior.gain_experience(100)
mage.gain_experience(150)
archer.gain_experience(120)

print("\nAfter combat:")
print(warrior.get_status())
print(mage.get_status())
print(archer.get_status())