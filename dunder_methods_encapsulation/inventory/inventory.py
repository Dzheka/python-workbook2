class Inventory:
    def __init__(self):
        self.items = {}

    def add(self, item_name, qty = 1):
        if item_name in self.items:
            self.items[item_name] += qty
        else:
            self.items[item_name] =  qty


    def remove(self, item, qty = 1):
        if item in self.items:
            self.items[item] -= qty
            if self.items[item] <= 0:
                del self.items[item]

    def __len__(self):
        return  len(self.items)

    def __contains__(self, item):
        if item in self.items:
            return True
        return False

    def __getitem__(self, item):
        return  self.items.get(item,0)

    def __add__(self, other):
        new_inv = Inventory()
        for item, qty in self.items.items():
            new_inv.add(item, qty)
        for item, qty in other.items.items():
            new_inv.add(item, qty)
        return new_inv

    def __eq__(self, other):
        return  self.items == other.items

    def __str__(self):
        result = "Inventory:\n"
        for item, qty in self.items.items():
            result += f"{item} x{qty}\n"

        return  result.strip()