from store import Inventory

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
    inv.export_csv(filename='inventory.csv')

if __name__ == '__main__':
    main()