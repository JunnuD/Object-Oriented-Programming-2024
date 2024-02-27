products = [("banana", 5.95), ("apple", 3.95), ("orange", 4.50), ("watermelon", 4.95)]

products.sort()

print ("Sort by the first item")
for product in products:
    print(product)

print()
print("Order by the second item in tuple")

def order_by_price(item: tuple):
    return item[1]


products1 = [("banana", 5.95), ("apple", 3.95), ("orange", 4.50), ("watermelon", 4.95)]

products1.sort(key=order_by_price)
for product in products1:
    print(product)


print()
print("Use sorted function")
products2 = [("banana", 5.95), ("apple", 3.95), ("orange", 4.50), ("watermelon", 4.95)]
t2 = sorted(products2, key=order_by_price)
for i in t2:
    print(i)


print()
for i in products2:
    print(i)

print()

def sort_by_price(items: list):
    return sorted(items, key=order_by_price)

products3 = [("banana", 5.95), ("apple", 3.95), ("orange", 4.50), ("watermelon", 4.95)]

for product in sort_by_price(products3):
    print(product)