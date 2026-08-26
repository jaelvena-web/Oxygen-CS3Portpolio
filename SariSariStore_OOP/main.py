class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Product: {self.name}")
        print(f"Price: P{self.price}")
        print(f"Quantity: {self.quantity}")

    def sell(self, quantity):
        if quantity <= 0:
            print("Quantity sold must be greater than 0.")
        elif quantity <= self.quantity:
            self.quantity -= quantity
            print(f"{quantity} {self.name}(s) sold.")
            print(f"Remaining quantity: {self.quantity}")
        else:
            print(f"Not enough stock to sell {quantity} {self.name}(s).")

    def restock(self, amount):
        if amount <= 0:
            print("Amount must be greater than 0.")
        else:
            self.quantity += amount
            print(f"{amount} {self.name}(s) restocked.")
            print(f"New quantity: {self.quantity}")

    def remove(self, amount):
        if amount <= 0:
            print("Amount must be greater than 0.")
        elif amount <= self.quantity:
            self.quantity -= amount
            print(f"{amount} {self.name}(s) removed.")
            print(f"New quantity: {self.quantity}")
        else:
            print(f"Not enough stock to remove {amount} {self.name}(s).")




def show_all_products(products_list):
    if not products_list:
        print("No products available.")
        return
    print("\n--- PRODUCT LIST ---")
    print(f"{'No.':<4}{'Product Name':<25}{'Price':<10}{'Quantity':<8}")
    print("-" * 50)
    for i, p in enumerate(products_list, 1):
        print(f"{i:<4}{p.name:<25}P{p.price:<9}{p.quantity:<8}")


def search_product(products_list, name):
    for p in products_list:
        if p.name.lower() == name.lower():
            print(f"\nFound: {p.name} | Price: P{p.price} | Qty: {p.quantity}")
            return p
    print(f"\nProduct '{name}' not found.")
    return None



product1 = Product("Lucky Me Pancit Canton", 15, 20)
product2 = Product("Coca Cola", 20, 10)
product3 = Product("Skyflakes", 10, 30)
product4 = Product("Piattos", 25, 12)
product5 = Product("Sardines", 30, 10)


products = [product1, product2, product3, product4, product5]


show_all_products(products)


search_product(products, "Piattos")


print("\n--- Product Operations ---")
product1.restock(15)
product3.remove(5)
product4.sell(1)


print("\n--- Updated Details ---")
product1.display_info()


show_all_products(products)

# Product list
products = {
    "lucky me pancit canton": {"price": 15, "qty": 17},
    "coca-cola": {"price": 25, "qty": 27},
    "skyflakes": {"price": 10, "qty": 50},
    "piattos": {"price": 25, "qty": 13},
    "sardines": {"price": 30, "qty": 22}
}

# 1. Display Products
print("--- PRODUCT LIST ---")
print("No. Name                       Price   Quantity")
i = 1
for name, info in products.items():
    print(f"{i:<4}{name.title():<27} ₱{info['price']:<7}{info['qty']}")
    i += 1

# 2. Search Product
search = input("\nSearch product: ").lower()
if search in products:
    print(f"Found: {search.title()} | Price: ₱{products[search]['price']} | Qty: {products[search]['qty']}")
else:
    print("Product not found.")

# 3. Update Price
item = input("\nEnter product to update price: ").lower()
if item in products:
    print(f"Old price: ₱{products[item]['price']}")
    products[item]['price'] = int(input("New price: ₱"))
    print("Price updated!")