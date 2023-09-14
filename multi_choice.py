
from integer_checker import integer_checker
from math_formulas import find_circle, find_quadralateral, find_trapezoid, find_triangle, see_history
import math

def multi_choice(option_amount):
  # Loop for testing
  while True:
    #Display choices, including example unicode
    choice = integer_checker("""Choose an option:
    1. \u25A1 Square
    2. \u25AD Rectangle
    3. \u25B1 Parallelogram
    4. \u25CB Circle
    5. \u25B3 Triangle
    6. \u23E2 Trapezoid
    7. History
    """, 7)
    #confirm interger input
    choice = int(math.floor(choice))
    # Branches
    if choice == 1 or choice == 2 or choice == 3:
      find_quadralateral(choice)
    if choice == 4:
      find_circle()
    if choice == 5:
      find_triangle()
    if choice == 6:
      find_trapezoid()
    if choice == 7:
      see_history()

    print("")
    continue
