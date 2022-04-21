print("**************************************")
print("**    Welcome to the Snakes Cafe!   **")
print("**    Please see our menu below.    **")
print("**")
print("**To quit at any time, type 'quit'**")
print("**************************************")

appetizers = ['Wings', 'Cookies', 'Spring Rolls']
entrees = ['Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden']
desserts = ['Ice Cream', 'Cake', 'Pie']
drinks = ['Coffee', 'Tea', 'Unicorn Tears']

print("""
Appetizers
----------""")
# for x in range(len(appetizers)):
#     # print(appetizers[x])
for appetizer in appetizers:
    print(appetizer)

print("""
Entrees
-------""")
for x in range(len(entrees)):
    print(entrees[x])

print("""
Desserts
--------""")
for x in range(len(desserts)):
    print(desserts[x])

print("""
Drinks
------""")
for x in range(len(drinks)):
    print(drinks[x])

print("***********************************")
print("** What would you like to order? **")
print("***********************************")

items = {}

while True:
    order = input('> ').capitalize()
    if order == 'quit':
        break
    elif order not in items:
        items[order] = 1
        
        print(f"** {items[order]} order of {order} have been added to your meal **")
    elif order in items:
        items[order] += 1
        print(f"** {items[order]} orders of {order} have been added to your meal **")
