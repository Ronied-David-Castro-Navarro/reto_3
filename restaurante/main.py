class MenuItem:

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def calculate_price(self) -> float:
        return self.price

class Beverage(MenuItem):
    def __init__(self, name: str, price: float, size: str):
        super().__init__(name, price)
        self.size = size

class Appetizer(MenuItem):
    def __init__(self, name: str, price: float, spicy: bool = False):
        super().__init__(name, price)
        self.spicy = spicy

class MainCourse(MenuItem):
    def __init__(self, name: str, price: float, portion_size: str = "regular"):
        super().__init__(name, price)
        self.portion_size = portion_size

class Order:
    def __init__(self):
        self.items: list[MenuItem] = []

    def add_item(self, item: MenuItem) -> None:
        self.items.append(item)

    def calculate_total(self) -> float:
        return sum(item.calculate_price() for item in self.items)

    def apply_discount(self) -> float:
        total = self.calculate_total()
        if len(self.items) >= 3:
            return total * 0.9
        return total

def main():
    menu = [
        Beverage("Coca Cola", 2.5, "medium"),
        Beverage("Water", 1.5, "small"),
        Beverage("Beer", 3.5, "large"),
        Appetizer("Arepa", 5.0, spicy=True),
        Appetizer("Cookies", 4.0),
        Appetizer("Chicken Wings", 6.0, spicy=True),
        MainCourse("Pizza", 12.0, portion_size="large"),
        MainCourse("Burger", 10.0),
        MainCourse("Pasta", 11.0),
        MainCourse("Salad", 8.0)
    ]

    order = Order()
    order.add_item(menu[0])
    order.add_item(menu[3])
    order.add_item(menu[6])

    print("------ Bill ------")
    for item in order.items:
        print(f"{item.name}: ${item.calculate_price():.2f}")

    print("------------------")
    print(f"Total without discount: ${order.calculate_total():.2f}")
    print(f"Total with discount: ${order.apply_discount():.2f}")


if __name__ == "__main__":
    main()
