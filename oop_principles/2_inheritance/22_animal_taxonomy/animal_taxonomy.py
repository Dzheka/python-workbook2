class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

    def move(self):
        return "Moving"

    def make_sound(self):
        return "..."


class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def make_sound(self):
        return "Woof! Woof!"

    def move(self):
        return "Running on four legs"

    def bark(self):
        print(f"{self.name} is barking loudly!")

    def fetch(self):
        print(f"{self.name} is fetching the ball!")

    def wag_tail(self):
        print(f"{self.name} is wagging its tail")


class Cat(Animal):
    def __init__(self, name, species, coat_color):
        super().__init__(name, species)
        self.coat_color = coat_color

    def make_sound(self):
        return "Meow! Meow!"

    def move(self):
        return "Stalking silently"

    def meow(self):
        print(f"{self.name} says meow")

    def purr(self):
        print(f"{self.name} is purring contentedly")

    def climb(self):
        print(f"{self.name} is climbing up the tree")


class Bird(Animal):
    def __init__(self, name, species, wingspan):
        super().__init__(name, species)
        self.wingspan = wingspan

    def make_sound(self):
        return "Tweet! Tweet!"

    def move(self):
        return "Flying with wings"

    def fly(self):
        print(f"{self.name} is flying gracefully")

    def sing(self):
        print(f"{self.name} is singing a beautiful song")

    def build_nest(self):
        print(f"{self.name} is building a nest")
