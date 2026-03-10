class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return f"{self.name} makes a sound!"

    def __repr__(self):
        return f"Animal(name='{self.name}', species='{self.species}')"



dog = Animal("Buddy", "Dog")
print(dog)          # Animal(name='Buddy', species='Dog')
dog.make_sound()    # Buddy makes a sound!