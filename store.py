

class Item:
    def __init__(self, name:str, price:float, quantity:int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name} ${round(self.price, 2)} {self.quantity}'

    def __repr__(self):
        return str(self)

class Inventory:
    def __init__(self, name):
        self.name = name
        self.items = {}

    def __str__(self):
        return f'{self.name} {list(self.items.values())}'

    def __repr__(self):
        return str(self)

    def add_item(self, item:Item):
        self.items[item.name] = item

    def add_item(self, name:str, price:float, quantity:int):
        self.items[name] = Item(name, price, quantity)
    
    def remove_item(self, name:str):
        return self.items.pop(name)
    
    def get_item(self, name:str):
        return self.items[name]

    def export_csv(self, filename:str):
        with open(filename, 'w') as f:
            f.write('Name,Price,Quantity\n')
            for item in self.items.values():
                f.write(f'{item.name},{item.price},{item.quantity}\n')


# TESTING

def main():
    inv = Inventory('Inventory')
    inv.add_item('apple', 1.99, 5)
    inv.add_item('banana', 2.99, 3)
    inv.add_item('orange', 3.99, 2)
    inv.add_item('pear', 4.99, 1)
    print(inv)
    inv.remove_item('apple')
    print(inv)
    print(inv.get_item('orange'))

if __name__ == '__main__':
    main()