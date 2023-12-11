class BasketModel:
    ITEMS = {
        "Luxury": {"price": 50, "vat": 0.20},
        "Essential": {"price": 30, "vat": 0.10},
        "Gift": {"price": 20, "vat": 0.05}
    }

    def __init__(self):
        self.basket = []

    def calculate_total(self, item_type, quantity):
        if item_type in self.ITEMS and quantity.isdigit():
            quantity = int(quantity)
            price = self.ITEMS[item_type]["price"]
            vat = self.ITEMS[item_type]["vat"]
            total = (price + price * vat) * quantity
            return total, vat
        else:
            return None, None

    def add_to_basket(self, item_type, quantity, total):
        if total is not None:
            self.basket.append((item_type, int(quantity), total))

    def get_basket_total(self):
        return sum(item[2] for item in self.basket)

    def get_basket_contents(self):
        return self.basket.copy()
