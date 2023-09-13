from integer_checker import integer_checker
from multi_choice import multi_choice
from math_formulas import find_square, find_parallelogram, find_rectangle, find_circle, find_triangle, find_trapezoid


print("Welcome. This is an area/perimeter calculator. To begin, type in the number of the shape you would like to use in calculation\n")

valid = True
while True:
  option = multi_choice(6)
