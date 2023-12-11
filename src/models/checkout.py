class ChangeCalculatorModel:
    def calculate_change(self, total_cost, amount_paid):
        if amount_paid < total_cost:
            return None, "Not enough money paid."

        change = amount_paid - total_cost
        denominations = [50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]
        change_distribution = {}

        for denomination in denominations:
            count, change = divmod(change, denomination)
            if count:
                change_distribution[denomination] = int(count)

        return change_distribution, ""
