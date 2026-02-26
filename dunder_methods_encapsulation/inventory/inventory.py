class Inventory:
    def __init__(self, items = {}):
        self.items = items

    def add(self, item, qty=1):
        qty.items += 1
        return Inventory(self.items + item.items)
    
    def remove(self, item, qty=1):
        qty.items -= 1
        return Inventory(self.items - item.items)
    
    def __len__(self):
        total = sum(self.items)

    def __contains__(self, item):
        pass


inv1 = Inventory()
inv1.add("Sword")
inv1.add("Potion", 3)
inv1.add("Shield")

print(len(inv1))           # 5
print("Potion" in inv1)    # True
print(inv1["Potion"])      # 3
print(inv1["Arrow"])       # 0

inv2 = Inventory()
inv2.add("Potion", 2)
inv2.add("Arrow", 10)

inv3 = inv1 + inv2
print(inv3["Potion"])      # 5
print(inv3["Arrow"])       # 10
print(inv3["Sword"])       # 1

inv1.remove("Potion", 2)
print(inv1["Potion"])      # 1