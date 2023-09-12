
from integer_checker import integer_checker
from math_formulas import find_circle, find_parellelogram, find_rectangle, find_square, find_trapezoid, find_triangle

def multi_choice(option_amount):
  # Loop for testing
  while True:
    choice = integer_checker("Choose an option: \n 1. Square \n 2. Rectangle \n 3. Parellelogram \n 4. Circle \n 5. Triangle \n 6. Trapezoid \n", 6)
    # Branches
    if choice == 1:
      find_square()
    if choice == 2:
      find_rectangle()
    if choice == 3:
      find_parellelogram()
    if choice == 4:
      find_circle()
    if choice == 5:
      find_triangle()
    if choice == 6:
      find_trapezoid()

    print("")
    continue