products = [("banana", 5.95), ("apple", 3.95), ("orange", 4.50), ("watermelon", 4.95)]

products.sort()

print ("Sort by the first item")
for product in products:
    print(product)

print("Order by the second item in tuple")

def order_by_price(item: tuple):
    return 

products1 = [("banana", 5.95), ("apple", 3.95), ("orange", 4.50), ("watermelon", 4.95)]

products1.sort(key=order_by_price)