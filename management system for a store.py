'''
NAME:Nandhakumar KS
DATE:19-11-2024
A retail store wants to create an inventory system that stores each item as a tuple
containing item name,quantity in stock,unit price.Define a list of tuples to represent
the inventory,also calculate and display the total stock value for each item.
'''

inventory = [
    ("Laptop", 5, 30000.00),
    ("Keyboard", 20,150.00),
    ("Mouse",50,150.00),
    ("Monitor",10,3000.00),
    ("Headphone",15,500.00),
]
highest_stock_value = 0
item_with_highest_stock_value =None
for item in inventory:
    item_name,quantity,unit_price = item
    stock_value = quantity*unit_price
    print(f"Item name:{item_name},the total value is: {stock_value}")
    if stock_value>highest_stock_value:
        highest_stock_value = stock_value
        item_with_highest_stock_value = item_name
print(f"Highest stock value is: {highest_stock_value}")
print(f"Item with the highest stock value is:{item_with_highest_stock_value}")