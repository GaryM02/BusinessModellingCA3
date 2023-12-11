import math


class PackingController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_box(self):
        self.model.add_box(self.view.box_length_entry.get(), self.view.box_width_entry.get(), self.view.box_height_entry.get(), self.view.box_weight_entry.get())
        self.view.show_box(self.model.box.__str__())

    def calculate_box_volume(self):
        box_volume = float(self.model.box.length) * float(self.model.box.width) * float(self.model.box.height)
        return box_volume
    
    def calculate_item_volume(self, length, width, height):
        item_volume = float(length) * float(width) * float(height)
        return item_volume
    
    def calculate_weight(self):
        box_weight = float(self.model.box.weight)
        return box_weight
    
    def calculate_volume_of_items(self):
        volume_of_items = 0
        for item in self.model.get_inventory_items():
            volume_of_items += self.calculate_item_volume(item.length, item.width, item.height)
        return volume_of_items
    
    def calculate_weight_of_items(self):
        weight_of_items = 0
        for item in self.model.get_inventory_items():
            weight_of_items += int(item.weight)
        return weight_of_items
    
    def calculate_boxes_needed(self):
        # Calculate the number of boxes needed based on volume and weight
        boxes_needed = self.calculate_number_of_boxes(self.model.get_inventory_items(), self.model.box)
     
        self.view.show_calculated_result(f"Boxes needed: {boxes_needed}")

    def show_items(self):
        self.view.retrival_function()
        self.items = self.model.get_inventory_items()
        if self.items:
            self.view.show_items(self.items)
        else:
            self.view.show_result("No items found.")

    def calculate_number_of_boxes(self, items, box):
        boxes_needed = 0
        temp_box_volume = self.calculate_box_volume()
        temp_box_weight = float(box.weight)
        # calculate boxes for volume
        # volume and weight can never exceed temp_box_volume and temp_box_weight
        # if volume exceeds temp_box_volume, then we need another box
        # if weight exceeds temp_box_weight, then we need another box
        # if both exceed, we need another box
        # if neither exceed, we can add the item to the box
        # if we can't add the item to the box, we need another box
        # if we can add the item to the box, we subtract the item's volume and weight from the temp_box_volume and temp_box_weight
        # we then repeat the process for the next item
        # we keep track of how many boxes we need for volume and weight
        # we then return the maximum of the two
        # if the maximum is a decimal, we round up to the nearest whole number
        # we then return the number of boxes needed
        # if the maximum is 0, we return 1
        for item in items:
            item_volume = self.calculate_item_volume(item.length, item.width, item.height)
            if item_volume >= temp_box_volume or float(item.weight) >= temp_box_weight:
                boxes_needed += 1
                temp_box_volume = self.calculate_box_volume()
                temp_box_weight = float(box.weight)
            else:
                temp_box_volume -= item_volume
                temp_box_weight -= float(item.weight)

        return math.ceil(boxes_needed) if boxes_needed > 0 else 1



   
