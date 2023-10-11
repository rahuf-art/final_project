# admin.py

class Admin:
    def __init__(self):
        self.food_items = []

    def add_food_item(self, name, quantity, price, discount, stock):
        # Generate FoodID automatically
        food_id = len(self.food_items) + 1
        food_item = {
            "FoodID": food_id,
            "Name": name,
            "Quantity": quantity,
            "Price": price,
            "Discount": discount,
            "Stock": stock,
        }
        self.food_items.append(food_item)

    # Other admin methods as before


    def edit_food_item(self, food_id, name, quantity, price, discount, stock):
        for item in self.food_items:
            if item["FoodID"] == food_id:
                item.update({
                    "Name": name,
                    "Quantity": quantity,
                    "Price": price,
                    "Discount": discount,
                    "Stock": stock
                })

    def view_food_items(self):
        return self.food_items

    def remove_food_item(self, food_id):
        self.food_items = [item for item in self.food_items if item["FoodID"] != food_id]
