class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display(self):
        print(f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def sell(self, qty):
        if qty <= self.quantity:
            self.quantity -= qty
            print(f"Sold {qty} units of {self.name}")
        else:
            print("Not enough stock!")

    def update_price(self, new_price):
        self.price = new_price
        print(f"Price of {self.name} updated to {self.price}")


products = []

while True:
    print("\n1. Add Product\n2. Sell Product\n3. Update Price\n4. Show Products\n5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter product name: ")
        price = float(input("Enter price: "))
        qty = int(input("Enter quantity: "))
        products.append(Product(name, price, qty))
    elif choice == "2":
        name = input("Enter product name to sell: ")
        qty = int(input("Enter quantity to sell: "))
        for p in products:
            if p.name == name:
                p.sell(qty)
                break
        else:
            print("Product not found!")
    elif choice == "3":
        name = input("Enter product name to update price: ")
        new_price = float(input("Enter new price: "))
        for p in products:
            if p.name == name:
                p.update_price(new_price)
                break
        else:
            print("Product not found!")
    elif choice == "4":
        for p in products:
            p.display()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")
