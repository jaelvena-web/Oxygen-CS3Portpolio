class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print("Product:", self.name)
        print("Price: P", self.price)
        print("Quantity:", self.quantity)

    def sell(self, quantity):
        if quantity <= self.quantity:
            self.quantity -= quantity
            print(quantity, self.name, "sold.")
        else:
            print("Not enough stock.")

    def restock(self, amount):
        if amount <= 0:
            print("Amount must be greater than 0.")
        else:
            self.quantity += amount
            print(amount, self.name, "restocked.")
            print("New quantity:", self.quantity)

    def remove(self, amount):
        if amount <= 0:
            print("Amount must be greater than 0.")
        elif amount <= self.quantity:
            self.quantity -= amount
            print(amount, self.name, "removed.")
            print("New quantity:", self.quantity)

        else:
           print("Not enough stock to remove.")

product1 = Product("Lucky Me Pancit Canton", 15, 20)
product1.display_info()
product2 = Product("Coca Cola", 20, 10)
product2.display_info()
product3 = Product("Skyflakes", 10, 30)
product3.display_info()
product4 = Product("Piattos", 25, 12)
product4.display_info()
product5 = Product("Sardines", 30, 10)
product5.display_info()

print("---Before Selling---")
product1.display_info()
print("Sell 3 Lucky Me Pancit Canton")
product1.sell(3)
print("---After Selling---")
product1.display_info()

print("---Restocking 10 items--")
product1.restock(10)
print("---After Restocking---")
product1.display_info()