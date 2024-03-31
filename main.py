class Item:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.name}, price: {self.price}"

class User:
    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name} {self.surname}"

class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user

    def add_item(self, item, cnt):
        if item in self.products:
            self.products[item] += cnt
        else:
            self.products[item] = cnt

    def __str__(self):
        output = f"User: {self.user}\nItems:\n"
        for item, quantity in self.products.items():
            output += f"{item.name}: {quantity} pcs.\n"
        return output

    def get_total(self):
        total = 0
        for item, quantity in self.products.items():
            total += item.price * quantity
        return total

lemon = Item('lemon', 5, "yellow", "small")
apple = Item('apple', 2, "red", "middle")

buyer = User("Ivan", "Ivanov", "02628162")

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
print("Total:", cart.get_total())

cart.add_item(apple, 10)
print(cart)
print("Total:", cart.get_total())
