class InventoryController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_item(self, name, item_type, expiration_date, length, width, height, weight):
        if name and item_type and expiration_date:
            item = self.model.add_item(name, item_type, expiration_date, length, width, height, weight)
            self.view.show_result(f"Item {name} added with ID {item.id}")
        else:
            self.view.show_result("All fields are required.")

    def view_items(self):
        items = self.model.get_items()
        self.view.show_items(items)

    def delete_item(self, item_id):
        self.model.delete_item(item_id)
        self.view_items()
