from admin import Admin
from user import User

def main():
    admin = Admin()
    user = User(admin)  # Create User instance without passing admin as an argument

    while True:
        print("Welcome to the Food Ordering App")
        print("1. Admin Login")
        print("2. User Register")
        print("3. User Login")
        choice = input("Enter your choice: ")

        if choice == '1':
            # Admin Login
            admin_username = input("Enter admin username: ")
            admin_password = input("Enter admin password: ")
            if admin_username == 'admin' and admin_password == 'admin':
                while True:
                    print("Admin Menu:")
                    print("1. Add Food Item")
                    print("2. Edit Food Item")
                    print("3. View Food Items")
                    print("4. Remove Food Item")
                    print("5. Logout")
                    admin_choice = input("Enter your choice: ")
                    if admin_choice == '1':
                        name = input("Enter food name: ")
                        quantity = input("Enter quantity: ")
                        price = float(input("Enter price: "))
                        discount = float(input("Enter discount: "))
                        stock = int(input("Enter stock: "))
                        admin.add_food_item(name, quantity, price, discount, stock)
                    elif admin_choice == '2':
                        food_id = int(input("Enter FoodID to edit: "))
                        name = input("Enter new name: ")
                        quantity = input("Enter new quantity: ")
                        price = float(input("Enter new price: "))
                        discount = float(input("Enter new discount: "))
                        stock = int(input("Enter new stock: "))
                        admin.edit_food_item(food_id, name, quantity, price, discount, stock)
                    elif admin_choice == '3':
                        print("Food Items:")
                        for item in admin.view_food_items():
                            print(item)
                    elif admin_choice == '4':
                        food_id = int(input("Enter FoodID to remove: "))
                        admin.remove_food_item(food_id)
                    elif admin_choice == '5':
                        break
                    else:
                        print("Invalid choice")

        elif choice == '2':
            # User Register
            full_name = input("Enter your full name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            password = input("Enter password: ")
            user.register(full_name, phone_number, email, address, password)

        elif choice == '3':
            # User Login
            email = input("Enter email: ")
            password = input("Enter password: ")
            if user.login(email, password):
                while True:
                    print("User Menu:")
                    print("1. Place New Order")
                    print("2. Order History")
                    print("3. Update Profile")
                    print("4. Logout")
                    user_choice = input("Enter your choice: ")
                    if user_choice == '1':
                        print("Available Food Items:")
                        food_items = admin.view_food_items()
                        for idx, item in enumerate(food_items, start=1):
                            print(f"{idx}. {item['Name']} ({item['Quantity']}) [INR {item['Price']}]")
                        selected_items = [int(x) for x in input("Enter the numbers of items you want to order (separated by space): ").split()]
                        order = user.place_order(selected_items)
                        print("Order Summary:")
                        for item in order["Items"]:
                            print(f"{item['Name']} ({item['Quantity']}) [INR {item['Price']}]")
                        print(f"Total Price: INR {order['Total Price']}")
                    elif user_choice == '2':
                        print("Order History:")
                        for idx, order in enumerate(user.order_history(), start=1):
                            print(f"Order {idx}:")
                            for item in order["Items"]:
                                print(f"{item['Name']} ({item['Quantity']}) [INR {item['Price']}]")
                            print(f"Total Price: INR {order['Total Price']}")
                    elif user_choice == '3':
                        new_data = {}
                        new_full_name = input("Enter new full name (Press Enter to skip): ")
                        if new_full_name:
                            new_data["Full Name"] = new_full_name
                        new_phone_number = input("Enter new phone number (Press Enter to skip): ")
                        if new_phone_number:
                            new_data["Phone Number"] = new_phone_number
                        new_address = input("Enter new address (Press Enter to skip): ")
                        if new_address:
                            new_data["Address"] = new_address
                        if new_data:
                            if user.update_profile(email, new_data):
                                print("Profile updated successfully!")
                            else:
                                print("Email not found.")
                    elif user_choice == '4':
                        break
                    else:
                        print("Invalid choice")

if __name__ == "__main__":
    main()
