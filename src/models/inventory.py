import uuid
from .item import Item

class InventoryModel:
    def __init__(self):
        self.items = []

    def add_item(self, name, item_type, expiration_date, length, width, height, weight):
        item_id = str(uuid.uuid4())
        
        itemmodel = Item(item_id, name, item_type, expiration_date, length, width, height, weight)
        
        self.items.append(itemmodel)
        return itemmodel

    def get_items(self):
        return self.items

    def delete_item(self, item_id):
        self.items = [item for item in self.items if item.get_id() != item_id]
