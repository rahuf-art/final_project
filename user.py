# user.py

class User:
    def __init__(self, admin):
        self.users = []
        self.orders = []
        self.admin = admin

    def register(self, full_name, phone_number, email, address, password):
        user_data = {
            "Full Name": full_name,
            "Phone Number": phone_number,
            "Email": email,
            "Address": address,
            "Password": password
        }
        self.users.append(user_data)

    # Other user methods as before


    def login(self, email, password):
        for user in self.users:
            if user["Email"] == email and user["Password"] == password:
                return True
        return False

    def place_order(self, food_items):
        order = {"Items": [], "Total Price": 0}
        for item in food_items:
            # Fetch the food item by ID from the admin's food_items list
            food_item = next((item for item in self.admin.food_items if item["FoodID"] == item), None)
            if food_item:
                order["Items"].append(food_item)
                order["Total Price"] += food_item["Price"]
        self.orders.append(order)
        print(self.orders.append(order))
        return order

    def order_history(self):
        return self.orders

    def update_profile(self, email, new_data):
        for user in self.users:
            if user["Email"] == email:
                user.update(new_data)
                return True
        return False
