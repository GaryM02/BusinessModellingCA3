

class PackingModel:
    def __init__(self):
        # items list will hold the items from the inventory
        self.inventory_items = []
        # box_dimensions will hold the dimensions of the box

    def add_box(self, length, width, height, weight):
        box = Box(length, width, height, weight)
        self.box = box

    def set_inventory_items(self, items):
        self.inventory_items = items

    def get_inventory_items(self):
        return self.inventory_items
    

class Box:
    def __init__(self, length, width, height, weight):
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight

    def __str__(self):
        return f"Box: {self.length}cm x {self.width}cm x {self.height}cm, {self.weight}kg"
    
