
from integer_checker import integer_checker

CAP = 100
PI = 3.14159265359

def find_square():
  print("SQUARE")
  base = integer_checker("Enter the length: ", CAP)
  perimeter = base * 4
  area = base * 2
  print("Area: {}, Perimeter: {}".format(area, perimeter))
  return

def find_rectangle():
  print("RECTANGLE")
  base = integer_checker("Enter the length: ", CAP)
  a = integer_checker("Enter the width: ", CAP)
  perimeter = base + base + a + a
  area = base * a
  print("Area: {}, Perimeter: {}".format(area, perimeter))
  return

def find_parellelogram():
  print("PARELLELOGRAM")
  base = integer_checker("Enter the base: ", CAP)
  a = integer_checker("Enter the height: ", CAP)
  perimeter = base + base + a + a
  area = base * a
  print("Area: {}, Perimeter: {}".format(area, perimeter))
  return

def find_circle():
  print("CIRCLE")
  base = integer_checker("Enter the radius: ", CAP)
  perimeter = 2 * PI * base
  area = PI * (base * base)
  print("Area: {}, Circumference: {}".format(area, perimeter))
  return

def find_triangle():
  print("TRIANGLE")
  base = integer_checker("Enter the base: ", CAP)
  a = integer_checker("Enter side A: ", CAP)
  b = integer_checker("Enter side B: ", CAP)
  c = integer_checker("Enter the height: ", CAP)
  perimeter = base + a + b
  area = 0.5 * base * c
  print("Area: {}, Perimeter: {}".format(area, perimeter))
  return
  
def find_trapezoid():
  print("TRAPEZOID")
  base = integer_checker("Enter the long base: ", CAP)
  a = integer_checker("Enter the short base: ", CAP)
  b = integer_checker("Enter side A: ", CAP)
  c = integer_checker("Enter side B: ", CAP)
  d = integer_checker("Enter the height: ", CAP)
  perimeter = base + a + b + c
  area = ((base + a)*0.5)*d
  print("Area: {}, Perimeter: {}".format(area, perimeter))
  return