
from integer_checker import integer_checker
from math_formulas import find_circle, find_parallelogram, find_rectangle, find_square, find_trapezoid, find_triangle
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
    """, 6)
    #confirm interger input
    choice = int(math.floor(choice))
    # Branches
    if choice == 1:
      find_square()
    if choice == 2:
      find_rectangle()
    if choice == 3:
      find_parallelogram()
    if choice == 4:
      find_circle()
    if choice == 5:
      find_triangle()
    if choice == 6:
      find_trapezoid()

    print("")
    continue
