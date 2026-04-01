class Animal:
    def init(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print(f"{self.name} makes a sound!")

    def repr(self):
        return f"Animal(name='{self.name}', species='{self.species}')"
