menu_intro = """**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************"""

appetizers = ['Wings', 'Cookies', 'Spring Rolls']
entrees = ['Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden']
desserts = ['Ice Cream', 'Cake', 'Pie']
drinks = ['Coffee', 'Tea', 'Unicorn Tears']
whole_menu = appetizers + entrees + desserts + drinks
total_order = {}

order_intro = """
***********************************
** What would you like to order? **
***********************************
"""

def print_section(section):
  for item in section:
    if item == section[0]:
      print(item)
      dashes ='-'*len(item)
      print(dashes)
    else:
      print(item)
  print('\n')




def take_order():
  while True:

    new_item = input('> ').title()

    print('\n')

    if new_item == 'Quit':
      break

    elif new_item not in whole_menu:
      print(f'** Sorry, but we don\'t make {new_item}')
    elif new_item not in total_order:
      total_order[new_item] = 1
      print(f'** 1 order of {new_item} has been added to your meal **')
    elif total_order[new_item] >= 1:
      total_order[new_item] += 1
      print(f'** Another order of {new_item} has been added **')
      print(f'** That makes {new_item} total **')

    print('** Would you like anything else? **')
    print('\n')


print(menu_intro)
print_section(appetizers)
print_section(entrees)
print_section(desserts)
print_section(drinks)
print(order_intro)
take_order()