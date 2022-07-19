

print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
""")
menu_items = ['wings', 'cookies', 'spring rolls', 'salmon', 'steak', 'meat tornado', 'a literal garden', 'ice cream', 'cake', 'pie', 'coffee', 'tea', 'unicorn tears']
order = input("> ")
if order == 'quit':
    exit()
elif order.lower() in menu_items:
    order_dict = {order: 1}
    print(f"** {order_dict[order]} order of {order} has been added to your meal ** \n")
else:
    print("Well that's not actually on our menu but I'll see what I can do for you...")
    order_dict = {order: 1}
    print(f"** {order_dict[order]} order of {order} has been added to your meal ** \n")

order2 = input("> ")
if order2 == 'quit':
    exit()
elif order2.lower() in menu_items:
    if order2 in order_dict:
        order_dict[order2] += 1
        print(f"** {order_dict[order2]} orders of {order2} have been added to your meal ** \n")
    else:
        order_dict[order2] = 1
        print(f"** {order_dict[order2]} order of {order2} has been added to your meal ** \n")
elif order2 in order_dict:
    print("Alright you know what?! Once was already too much! \n If you're not gonna order off our menu then just leave!")
    print("\n...You've been kicked out of Snakes Cafe...")
    exit()
else:
    print("Well that's not actually on our menu but I'll see what I can do for you...")
    order_dict[order2] = 1
    print(f"** {order_dict[order2]} order of {order2} has been added to your meal ** \n")

def repeat_order():
    summary = order_dict.items()
    print("Ok so altogether that's:")
    for item in summary:
        print(f"{item[1]} order of {item[0]}")

order3 = input("type 'done' below to place your order... \n or type anything else to cancel your order... \n> ")
if order3 == 'done':
    repeat_order()
else:
    exit()










# class Order:
#     def __init__(self, item):
#     self.orderSoFar = []
#     self.count = 0
#
#     def add_1_to_count(self):
#         self.count += 1
#
#     def repeat_order_to_customer(self):
#         if self.count == 1:
#             print(f"** {self.count} order of {self.item} has been added to your meal **")
#         elif self.count >1:
#             print(f"** {self.count} orders of {self.item} have been added to your meal **")

# def add_to_order(item):
#     if not len(order_dict):
#         order_dict = {item: 1}
#         print(order_dict)
#     elif item in order_dict:
#         order_dict[item] += 1
#         print(order_dict)
#
#     print("order = input("> ")")
#
# add_to_order(order)
# def process(newOrder):
#
#     orderSoFar = []
#     orderSoFar.append(newOrder)
#     if len(orderSoFar) == 1:
#         print(f"** 1 order of {orderSoFar[0]} have been added to your meal **" )
#     #elif len(orderSoFar) > 1:
#
# process(order)
#
# def count_ticker(item):
#     itemCount = 0
