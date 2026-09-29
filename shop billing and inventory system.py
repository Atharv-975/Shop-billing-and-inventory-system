product = { 101: {"name": "Rice", "price": 60, "stock": 120},
            102: {"name": "Wheat", "price": 45, "stock": 30},
            103: {"name": "Sugar", "price": 50, "stock": 60},
            104: {"name": "Milk", "price": 30, "stock": 50},
            105: {"name": "Biscuits", "price": 25, "stock": 130},
            106: {"name": "Tea powder", "price": 120, "stock": 110},
            107: {"name": "Cooking Oil", "price": 140, "stock": 115},
            108: {"name": "Soap", "price": 35, "stock": 135},
            109: {"name": "Shampoo", "price": 90, "stock": 120},
            110: {"name": "Toothpaste", "price": 70, "stock": 140},
            111: {"name": "Salt", "price": 25, "stock": 150},
            112: {"name": "all Types of Juice", "price": 80, "stock": 120},
            113: {"name": "Chocolate", "price": 50, "stock": 180} }

def display_product():
    print("\n==============")
    print("Product inventory")
    print("==============")
    print("ID | product | price | stock")
    print("==============")

    for product_id, item in product.items():
        print(product_id, "|", item["name"], "| Rs", item["price"], "|", item["stock"])
    print("==============")


def search_product():             # search product
    name= input("\nenter product name to search: ").lower()
    found = False

    for product_id, item in product.items():
        if name in item["name"].lower():
            print("ID:",product_id, "| product:",item["name"], "| price: Rs",item["price"], "| stock:",item["stock"])
            found = True

    if not found:
        print("product not found")

def add_product():             # add product
    print("\n-----Add new product-----")

    product_id= int(input("Enter product ID: "))
    if product_id in product:
        print("Product ID exists")
        return

    name= input("enter product name: ")
    price= float(input("enter price: "))
    stock= int(input("enter stock quantity: "))
    product[product_id] = {"name":name, "price":price, "stock":stock}

    print("Product added successfully")

# update stock
def updated_stock():
    display_product()
    product_id= int(input("\nenter product ID: "))
    if product_id not in product:
        print("Product not found")
        return
    
    quantity= int(input("enter quantity to add: "))
    if quantity <= 0:
        print("quantity must be greater than zero")
        return
    product[product_id]["stock"] +=quantity

    print("Stock updated successfully")
    print("New stock for", product[product_id]["name"], ":", product[product_id]["stock"])


market_name= "Fresh @ Shop"          # info and bill
market_phone= "9876543210"

def generate_bill():
    print("\n==== Create Bill ====")
    cart=[]

    display_product()
    while True:
        product_id= int(input("\nenter product ID (0 to finish): "))
        if product_id== 0:
            break

        if product_id not in product:
            print("product not found")
            continue

        item = product[product_id]
        if item["stock"] == 0:
            print("Sorry! this product is out of stock")
            continue
        
        quantity= int(input("enter quantity: "))
        if quantity <= 0:
            print("quantity must be greater than zero")
            continue

        if quantity > item["stock"]:
            print("Only", item["stock"], "products are available")
            continue
        amount= item["price"] * quantity

        cart.append({"id":product_id, "name":item["name"], "price":item["price"], "quantity":quantity, "amount":amount})
        item["stock"] -=quantity
        print(quantity, item["name"], "added to cart")

    if len(cart) ==0:
        print("\nNo product added to bill")
        return

    subtotal= 0
    for item in cart:
        subtotal +=item["amount"]

    if subtotal >= 4000:
        discount_rate = 4
    elif subtotal >= 1500:
        discount_rate = 2
    else:
        discount_rate =0

    discount= subtotal * discount_rate /100
    amount_after_discount= subtotal - discount
    grand_total= amount_after_discount


    print("\n============================")        # bill
    print(market_name)
    print("Customer Bill")
    print("============================")

    print("Phone: ",market_phone)
    print("============================")
    print("Item          Price   QTY   Total")
    print("====================")

    for item in cart:
        print(item["name"], "Rs", item["price"], " x ", item["quantity"], " = Rs", item["amount"])

    print("====================")
    print("Subtotal: Rs",subtotal)
    print("Discount: Rs",discount)
    print("Amount After Discount: Rs",amount_after_discount)
    print("====================")
    print("Grand Total: Rs",grand_total)
    print("=====================")


    print("\nPayment option")
    print("1. cash")
    print("2. UPI")
    print("3. card")

    payment = input("choose payment method: ")
    if payment == "1":
        payment_method = "cash"
    elif payment == "2":
        payment_method = "UPI"
    else:
        payment_method = "card"
    print("\nPayment method: ",payment_method)
    print("Amount paid: Rs",grand_total)

    print("=============================")
    print("Thank you for shopping with us!", "visit again")
    print("=============================")

def main():
    while True:
        print("\n===========================")
        print("Fresh @ Shop")
        print("===========================")
        print("1. View inventory")
        print("2. Search product")
        print("3. Add New product")
        print("4. Updated stock")
        print("5. Generate customer bill")
        print("6. Exit")
        print("===========================")

        choice = input("enter your choice: ")
        if choice== "1":
            display_product()
        elif choice== "2":
            search_product()
        elif choice== "3":
            add_product()
        elif choice== "4":
            updated_stock()
        elif choice== "5":
            generate_bill()
        elif choice== "6":
            print("Have a nice day!")
            break
        else:
            print("\nInvalid choice")
            print("select number from 1 to 6")
main()