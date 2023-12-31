import csv


class Item:
    pay_rate = 0.8  # 20% discount on all items - this is a magic attribute / class attribute
    all = []  # this is a magic attribute / class attribute

    def __init__(self, name: str, price: int, quantity: int):
        # data validation
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"

        # assigning the values to the object's properties
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

        print(f"Item created, name : {name}")

    def calculate_total_price(self):
        return self.price * self.quantity

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))

            )

    @staticmethod
    def is_integer(num):
        # we will count out the floats that are point zer

        if isinstance(num, float): # this will convert the float to int
            return num.is_integer()
        elif isinstance(num, int):
            return True
        return False


    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


# Item.instantiate_from_csv()
# print(Item.all)

print(Item.is_integer(1.8))