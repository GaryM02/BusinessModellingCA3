


class Item:
    def __init__(self, uuid, name, type, date, length, width, height, weight):
        self.id = uuid
        self.name = name
        self.type = type
        self.date = date
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight

    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_date(self):
        return self.date

    def set_name(self, name):
        self.name = name

    def set_type(self, type):
        self.type = type

    def set_date(self, date):
        self.date = date

    def get_length(self):
        return self.length
    
    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def get_weight(self):
        return self.weight
    
    def set_length(self, length):
        self.length = length

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def set_weight(self, weight):
        self.weight = weight

    def __str__(self):
        return f"{self.name} {self.id}"