class Inventory:
    def __init__(self):
        self.items = {}

    def add(self, item, qty=1):
        if qty > 0:
            self.items[item] = self.items.get(item, 0) + qty

    def remove(self, item, qty=1):
        if item in self.items and qty > 0:
            self.items[item] -= qty
            if self.items[item] <= 0:
                del self.items[item]

    def __len__(self):
        return sum(self.items.values())

    def __contains__(self, item):
        return item in self.items

    def __getitem__(self, item):
        return self.items.get(item, 0)

    def __add__(self, other):
        if not isinstance(other, Inventory):
            return NotImplemented
        new_inv = Inventory()
        for item, qty in self.items.items():
            new_inv.add(item, qty)
        for item, qty in other.items.items():
            new_inv.add(item, qty)
        return new_inv

    def __eq__(self, other):
        if not isinstance(other, Inventory):
            return False
        return self.items == other.items

    def __str__(self):
        if not self.items:
            return "Inventory is empty."
        lines = ["=== Inventory ==="]
        for item, qty in sorted(self.items.items()):
            lines.append(f"{item} x{qty}")
        lines.append(f"Total items: {len(self)}")
        return "\n".join(lines)
