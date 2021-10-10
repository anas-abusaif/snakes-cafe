print(
    """
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
  """
)

menu = [
    "Wings",
    "Cookies",
    "Spring Rolls",
    "Salmon",
    "Steak",
    "Meat Tornado",
    "A Literal Garden",
    "Ice Cream",
    "Cake",
    "Pie",
    "Coffee",
    "Tea",
    "Unicorn Tears",
]
showing = True
order = []
items_count = {}
while showing:
    raw_input = list(input(">>>"))
    raw_input[0] = raw_input[0].upper()
    item = "".join(raw_input)
    if item == "Quit":
        print(
            """
        
                     ** your order **
        """
        )
        for i in items_count:
            print(f"                        {items_count[i]} {order[order.index(i)]}")
        print(
            """
        
        ** Thank you for oredering from Snakes Cafe **
        """
        )
        showing = False
    elif item in menu:
        if item in order:
            items_count[item] += 1
            print(f"{items_count[item]} oreders of {order[order.index(item)]} have been added to your meal **")
        else:
            order.append(item)
            items_count[item] = 1
            print(f"{items_count[item]} oreders of {order[order.index(item)]} have been added to your meal **")
    else:
        print(
            "Sorry! this item is not available, please select something from the menu"
        )
