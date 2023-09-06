
from integer_checker import integer_checker

def multi_choice(option_amount):
  # Loop for testing
  while True:
    choice = integer_checker("Choose an option, 1-{}: ".format(option_amount), option_amount)
    # Branches
    if choice == 1:
      print("One")
    if choice == 2:
      print("Two")
    if choice == 3:
      print("Three")
    if choice == 4:
      print("Four")
    if choice == 5:
      print("Five")
    if choice == 6:
      print("Six")

    continue