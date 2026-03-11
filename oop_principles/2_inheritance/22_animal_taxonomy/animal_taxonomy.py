class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def eat(self):
        return f"{self.name} is eating"

    def sleep(self):
        return f"{self.name} is sleeping"

    def move(self):
        return f"{self.name} is moving"
    
    def make_sound(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def make_sound(self):
        return "Woof! Woof!"
    
    def move(self):
        return "Running on four legs"
    
    def bark(self):
        return f"{self.name} is barking loudly"

    def fetch(self):
        return f"{self.name} is fetching the ball"

    def wag_tail(self):
        return f"{self.name} is wagging its tail"

class Cat(Animal):
    def __init__(self, name, species, coat_color):
        super().__init__(name, species)
        self.coat_color = coat_color

    def make_sound(self):
        return "Meow! Meow!"
    
    def move(self):
        return "Stalking silently"
    
    def meow(self):
        return f"{self.name} is meowing softly"

    def purr(self):
        return f"{self.name} is purring contentedly"

    def climb(self):
        return f"{self.name} is climbing up the tree"

class Bird(Animal):
    def __init__(self, name, species, wingspan):
        super().__init__(name, species)
        self.wingspan = wingspan

    def make_sound(self):
        return "Tweet! Tweet!"
    
    def move(self):
        return "Flying with wings"
    
    def fly(self):
        return f"{self.name} is flying gracefully"

    def sing(self):
        return f"{self.name} is singing a beautiful song"

    def build_nest(self):
        return f"{self.name} is building a nest"

# Create different animals
dog = Dog("Buddy", "Golden Retriever", "Golden Retriever")
cat = Cat("Whiskers", "Domestic Cat", "Orange")
bird = Bird("Tweety", "Canary", 0.15)

# Display basic information
print(f"Dog: {dog.name} ({dog.species})")
print(f"Breed: {dog.breed}")
print(f"Sound: {dog.make_sound()}")
print(f"Movement: {dog.move()}")
dog.bark()
dog.fetch()

print(f"\nCat: {cat.name} ({cat.species})")
print(f"Color: {cat.coat_color}")
print(f"Sound: {cat.make_sound()}")
print(f"Movement: {cat.move()}")
cat.purr()
cat.climb()

print(f"\nBird: {bird.name} ({bird.species})")
print(f"Wingspan: {bird.wingspan}m")
print(f"Sound: {bird.make_sound()}")
print(f"Movement: {bird.move()}")
bird.fly()
bird.sing()

# Demonstrate polymorphism
animals = [dog, cat, bird]
print("\nAll animals making sounds:")
for animal in animals:
    print(f"{animal.name}: {animal.make_sound()}")

print("\nAll animals moving:")
for animal in animals:
    print(f"{animal.name}: {animal.move()}")