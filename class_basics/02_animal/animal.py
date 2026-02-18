class Animal():
    def __init__(self, name, species)->None:
        self.name = name
        self.species = species

    def __repr__(self) ->str:
        return f"Animal(name='{self.name}', species='{self.species}')"

    def make_sound(self):
        print(f"{self.name} makes a sound!")

dog = Animal("Buddy", "Dog")
print(dog)  
dog.make_sound()
