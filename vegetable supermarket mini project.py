vegetables = ["carrot", "potato", "onion", "ladyfinger"]
quantity = [50, 40, 80, 30]
cost_price = [35, 55, 50, 40]
selling_price = [45, 65, 60, 50]
total_revenue = 0
total_cost = 0
individual_revenue = [0] * len(vegetables)
customers = []

print("WELCOME TO ANVITHA SUPERMART")

while True:
    print("\nSelect user type:")
    print("1. owner")
    print("2. customer")
    ch = input("Are you owner or customer: ")

    # ---------------- CUSTOMER SECTION ----------------
    if ch == "2" or ch.lower() =="customer":
        print("WELCOME CUSTOMER!")
        while True:
            customer_name = input("Enter your name: ")
            if customer_name.strip():
                break
            else:
                print("Invalid name. Please enter again.")

        while True:
            phone_number = input("Enter your phone number: ")
            if phone_number.isdigit() and len(phone_number) == 10:
                break
            else:
                print("Invalid phone number. Please enter a 10-digit number.")

        cart = []
        total_revenue = 0
        total_cost = 0
        customer_details = {"name": customer_name, "phone": phone_number, "cart": cart}
        customers.append(customer_details)

        while True:
            print("\n1. Display items")
            print("2. Add to cart")
            print("3. View cart")
            print("4. Modify cart")
            print("5. Generate bill")
            print("6. Exit")

            ch = input("Choose an option: ")

            if ch == "1":
                print("\nItems available:")
                for i in range(len(vegetables)):
                    print(f"{vegetables[i]} - Quantity: {quantity[i]} kg, Cost Price: Rs.{cost_price[i]}")

            elif ch == "2":
                item = input("Which vegetable do you want to add to the cart: ").lower()
                if item in vegetables:
                    qty = float(input("How much quantity do you want (in kgs): "))
                    idx = vegetables.index(item)
                    if qty <= quantity[idx]:
                        amount = qty * selling_price[idx]
                        print("Added to cart. Amount: Rs.", amount)
                        total_revenue += amount
                        total_cost += qty * cost_price[idx]
                        quantity[idx] -= qty
                        cart.append((item, qty, amount))
                        individual_revenue[idx] += amount
                    else:
                        print("Out of stock!")
                else:
                    print("Item not available!")

            elif ch == "3":
                print("\nYour cart:")
                if cart:
                    for item, qty, amount in cart:
                        print(f"{item} - Quantity: {qty} kg, Amount: Rs.{amount}")
                else:
                    print("Your cart is empty.")

            elif ch == "4":
                if not cart:
                    print("Your cart is empty, nothing to modify.")
                    continue

                print("\nItems in your cart:")
                for i, (item, qty, amount) in enumerate(cart, start=1):
                    print(f"{i}. {item} - Quantity: {qty} kg, Amount: Rs.{amount}")

                item = input("Enter the name of the item you want to modify: ").lower()
                if item in [x[0] for x in cart]:
                    idx = [x[0] for x in cart].index(item)
                    veg_idx = vegetables.index(item)

                    old_qty = cart[idx][1]
                    print(f"Current quantity of {item}: {old_qty} kg")
                    new_qty = float(input("Enter new quantity (in kgs): "))
                    quantity[veg_idx] += (old_qty - new_qty)
                    new_amount = new_qty * selling_price[veg_idx]
                    cart[idx] = (item, new_qty, new_amount)
                    total_revenue = sum(a for _, _, a in cart)

                    print(f"Item '{item}' updated successfully!")
                    print(f"New quantity: {new_qty} kg, New amount: Rs.{new_amount}")
                else:
                    print("Item not found in cart!")

            elif ch == "5":
                print("\nGenerating bill...")
                if cart:
                    print("------ BILL ------")
                    for item, qty, amount in cart:
                        print(f"{item} - Quantity: {qty} kg, Amount: Rs.{amount}")
                    print("Total Amount: Rs.", total_revenue)
                    print("Thank you for shopping with us!")
                else:
                    print("Your cart is empty. Nothing to bill.")

            elif ch == "6":
                print("Exiting customer section...")
                break

            else:
                print("Invalid option! Please choose again.")

    # ---------------- OWNER SECTION ----------------
    elif ch == "1" or ch.lower()=="owner":
        while True:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            owner_username = "sai"
            owner_password = "Teja@143"

            if username == owner_username and password == owner_password:
                print("Login successful! Welcome, owner.")
                break
            else:
                print("Incorrect username or password. Please try again.")

        while True:
            print("\n1. Display items")
            print("2. Add item")
            print("3. Remove item")
            print("4. Modify item")
            print("5. View total revenue")
            print("6. View profit/loss")
            print("7. View customers")
            print("8. Generate report")
            print("9. Logout")

            ch = input("Choose an option: ")

            if ch == "1":
                print("\nItems available:")
                for i in range(len(vegetables)):
                    print(f"{vegetables[i]} - Quantity: {quantity[i]}, Cost: {cost_price[i]}, Selling: {selling_price[i]}")

            elif ch == "2":
                item = input("Enter the vegetable name: ").lower()
                if item in vegetables:
                    idx = vegetables.index(item)
                    qty = int(input("Enter new quantity: "))
                    cost = int(input("Enter new cost price: "))
                    sell = int(input("Enter new selling price: "))
                    quantity[idx] = qty
                    cost_price[idx] = cost
                    selling_price[idx] = sell
                    print("Item updated successfully.")
                else:
                    qty = int(input("Enter quantity: "))
                    cost = int(input("Enter cost price: "))
                    sell = int(input("Enter selling price: "))
                    vegetables.append(item)
                    quantity.append(qty)
                    cost_price.append(cost)
                    selling_price.append(sell)
                    individual_revenue.append(0)
                    print("New item added successfully!")

            elif ch == "3":
                item = input("Which vegetable do you want to remove: ").lower()
                if item in vegetables:
                    idx = vegetables.index(item)
                    vegetables.pop(idx)
                    quantity.pop(idx)
                    cost_price.pop(idx)
                    selling_price.pop(idx)
                    individual_revenue.pop(idx)
                    print("Item removed successfully!")
                else:
                    print("Item not found!")

            elif ch == "4":
                item = input("Which vegetable do you want to modify: ").lower()
                if item in vegetables:
                    idx = vegetables.index(item)
                    qty = int(input("Enter new quantity: "))
                    cost = int(input("Enter new cost price: "))
                    sell = int(input("Enter new selling price: "))
                    quantity[idx] = qty
                    cost_price[idx] = cost
                    selling_price[idx] = sell
                    print("Item modified successfully!")
                else:
                    print("Item not found in inventory.")

            elif ch == "5":
                print(f"Total Revenue: Rs.{total_revenue}")

            elif ch == "6":
                print(total_revenue)
                print(total_cost)
                profit_loss = total_revenue - total_cost
                if profit_loss > 0:
                    print(f"Profit: Rs.{profit_loss}")
                elif profit_loss < 0:
                    print(f"Loss: Rs.{-profit_loss}")
                else:
                    print("No profit, no loss.")

            elif ch == "7":
                print("\nCustomer Details:")
                if customers:
                    for customer in customers:
                        print(f"Name: {customer['name']}, Phone: {customer['phone']}")
                        print("Cart:")
                        for item, qty, amount in customer["cart"]:
                            print(f"  {item} - {qty}kg - Rs.{amount}")
                        print("-" * 30)
                else:
                    print("No customers yet.")

            elif ch == "8":
                ch = input("Do you want to close the shop (yes/no): ").lower()
                if ch == "yes":
                    print("\n------ REPORT ------")
                    print(f"Total Revenue: Rs.{total_revenue}")
                    profit_loss = total_revenue - total_cost
                    if profit_loss > 0:
                        print(f"Profit: Rs.{profit_loss}")
                    elif profit_loss < 0:
                        print(f"Loss: Rs.{-profit_loss}")
                    else:
                        print("No profit, no loss.")

                    print("\nRemaining Inventory:")
                    for i in range(len(vegetables)):
                        print(f"{vegetables[i]} - Quantity: {quantity[i]}, Cost: {cost_price[i]}, Selling: {selling_price[i]}")

                    print("\nIndividual Item Revenue:")
                    for i in range(len(vegetables)):
                        print(f"{vegetables[i]} - Revenue: Rs.{individual_revenue[i]}")

                    print("\nCustomer Summary:")
                    if customers:
                        for customer in customers:
                            print(customer)
                    else:
                        print("No customers have made purchases yet.")
                    break

            elif ch == "9":
                print("Logging out...")
                break

            else:
                print("Invalid choice! Please try again.")

    else:
        print("Invalid user type! Please enter 'owner' or 'customer'.")

