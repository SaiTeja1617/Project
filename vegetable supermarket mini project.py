vegetables=["carrot","potato","onion","ladyfinger"]
quantity=[50,40,80,30]
cost_price=[35,55,50,40]
selling_price=[45,65,60,50]
total_revenue=0
total_cost=0
individual_revenue=[0]*len(vegetables)  
customers=[]


print(""*10,"WELCOME TO SUPERMART ",""*10)
while True:
    print("owner")
    print("customer")
    ch=input("Are you owner are customer:")

#customer
 
    if ch=="customer":
        print("WELCOME")
        while True:
            customer_name=(input("Enter your name:"))
            if customer_name:
                break
        else:
            print("Invalid name")
            print("Please enter the correct name:")
        
        while True:
            phone_number=(input("Enter your phone number:"))
            if phone_number.isdigit() and len(phone_number)==10:
                break
            else:
                print("Invalid phone number")
                print("Please enter the correct phone number:")

       
        cart=[]
        total_revenue=0
        total_cost=0
        customer_details={"name":customer_name,"phone":phone_number,"cart":cart}
        customers.append(customer_details)

        while True:
            print("1.display items")
            print("2.add to cart")
            print("3.view cart")
            print("4.modify cart")
            print("5.bill")
            print("6.exit")

            ch=input("choose an option:")

            if ch=="1":
                print("Items available:")
                for i in range(len(vegetables)):
                    print("{}- quantity:{} kg,cost price: Rs.{}". format(vegetables[i],quantity[i],cost_price[i]))
                    
            elif ch=="2":
                item=input("Which vegetables do you want to add to the cart:")
                if item in vegetables:
                    qty=float(input("How much quantity do you want(in kgs):"))
                    idx=vegetables.index(item)
                    if qty<=quantity[idx]:
                        amount=qty*selling_price[idx]
                        print("added to cart.amount:Rs.",amount)
                        total_revenue+=amount
                        total_cost+=qty*cost_price[idx]
                        quantity[idx]-=qty
                        cart.append((item,qty,amount))
                        individual_revenue[idx] += amount
                    else:
                        print("Out of stock")
                else:
                    print("Item is not available")
             
            elif ch=="3":
                print("Your cart")
                if cart:
                    for item,qty,amount in cart:
                         print("{}- quantity:{} kg,amount: Rs.{}". format(item,qty,amount))
                else:
                    print("Your cart is empty")
            elif ch=="4":
                item=input("Which item do you want to modify:")
                if item in [x[0] for x in cart]:
                    new_qty=float(input("Enter new quantity:"))
                    idx=[x[0] for x in cart].index(item)
                    veg_idx=vegetables.index(item)                          
                    old_qty=cart[idx][1]
                    new_amount = new_qty * selling_price[veg_idx]
                    quantity[veg_idx]+=(old_qty-new_qty)
                    cart[idx]=(item,new_qty,new_qty*selling_price[veg_idx])
                    print("Item modify successfully")
                    individual_revenue[veg_idx] += (new_amount - cart[idx][2])
                else:
                    print("Item not in cart")

            elif ch=="5":
                print("Generating bill...")
                if cart:
                    print("Your bill")
                    for item,qty,amount in cart:
                        print("{} - quantity: {} kg,amount: Rs.{}".format(item,qty,amount))
                    print("Total amount: Rs",total_revenue)
                    print("Thank you for shopping with us")
                else:
                    print("Your cart is empty,nothing to bill")

            elif ch=="6":
                print("Exiting...")
                
                break
            else:
                print("Invalid option,please choose again")
                break

#owner

    elif ch=="owner":
        while True:
            username=input("Enter your usename:")
            password=input("Enter your password:")
            owner_username="sai"
            owner_password="Teja@143"
            if username==owner_username and password==owner_password:
                print("Login successfully")
                print("Hi,owner")
                break
            else:
                print("username or password is not correct")
                print("please try again")
    

        while True:
            
            print("1.Display items")
            print("2.Add item")
            print("3.Remove item")
            print("4.Modify item")
            print("5.View total revenue")
            print("6.View profit/loss")
            print("7.View customers")
            print("8.Generate report")
            print("9.Logout")

            ch=input("Choose an option:")

            if ch=="1":
                 print("Items available")
                 for i in range(len(vegetables)):
                     print("{}-quantity:{},cost price:{},selling  price:{}".format(vegetables[i],quantity[i],cost_price[i],selling_price[i]))
              
        
            elif ch=="2":
                item=input("Which vegetable do you want to add:")
		if item in vegetables:
		    idx=vegetables.index(item)    
		    qty=int(input("Enter new quantity:"))
		    cost=int(input("Enter new cost price:"))
                    sell=int(input("Enter new selling price:"))
                    quantity[idx]=qty
                    cost_price[idx]=cost
                    selling_price[idx]=sell
                    print("Item modified successfully:")
		    
		else:
                    vegetables.append(item)
                    qty=int(input("Enter quantity of item:"))
                    cost=int(input("Enter cost price of item:"))
                    sell=int(input("Enter selling price of item:"))
                    quantity.append(qty)
                    cost_price.append(cost)
                    selling_price.append(sell)
                    print("Item is added successfully")
            elif ch=="3":
                item=input("Which vegatables do you want to remove:")
                if item in vegetables:
                    price1=int(input("item of the price is removed:"))
                    quantity1=int(input("quantity is removed:"))
                    idx=vegetables.index(item)
                    vegetables.remove(item)
                    cost_price.remove(price1)
                    quantity.remove(quantity1)
                    
                    print(vegetables)
                    print(price1)
                    print(quantity1)
                    
                   
                    print("Item is removed successfully")
                
                
            elif ch=="4":
                item=input("Which vegetable do you want to modify:")
                if item in vegetables:
                    idx=vegetables.index(item)
                    qty=int(input("Enter new quantity:"))
                    cost=int(input("Enter new cost price:"))
                    sell=int(input("Enter new selling price:"))
                    quantity[idx]=qty
                    cost_price[idx]=cost
                    selling_price[idx]=sell
                    print("Item modified successfully:")
                else:
                    print("Item is not in the inventory")
            elif ch=="5":
                print("Total revenue: Rs. {}".format(total_revenue))
            elif ch=="6":
                profit_loss=total_revenue-total_cost
                if profit_loss > 0:
                    print("profit:{}". format(profit_loss))
                elif profit_loss < 0:
                    print("loss:{}". format(-profit_loss))
                else:
                    print("no profit,no loss")
            elif ch=="7":
                print("customer details:")
                if customers:
                    for customer in customers:
                        print("Name: {},phone:{}".format(customer["name"],customer["phone"]))
                        print("cart:")
                        for item,qty,amount in customer["cart"]:

                            print("{} - quantity: {} kg,amount: Rs.{}". format(item,qty,amount))
                        print("-"*30)
                else:
                    print("no customers have made purchases yet")

            elif ch=="8":
               
               ch=input("do you want to close the shop(yes/no):")
               if ch=="yes":
                   print(""*10,"REPORT",""*10)
                   print("Generating report....")
                   print("total revenue: Rs. {}". format(total_revenue))
                   profit_loss=total_revenue-total_cost
                   if profit_loss>0:
                       print("profit: Rs.{}".format(profit_loss))
                   elif profit_loss<0:
                       print("loss: Rs.{}".format(-profit_loss))
                   else:
                       print("no profit,no loss")
                   print("Remaining inventory:")
                   for i in range(len(vegetables)):
                       print("{} - quantity: {}, cost price: Rs. {}, selling price: Rs. {}". format(vegetables[i],quantity[i],cost_price[i],selling_price[i]))
                   print("individual item revenue:")
                   for i in range(len(vegetables)):
                       print("{} - revenue: Rs. {}".format(vegetables[i],individual_revenue[i]))
                   print("customers")
                   if customers:
                       for customer in customers:
                           print(customer)
                   else:
                       print("no customers have made purchases yet")
                   break
            elif ch=="9":
                print("log out")
                print("Thank you")
                break
                

           
            else:
                print("Invalid choice")
                print("Please try again")
        break
