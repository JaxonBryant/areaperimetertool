
from integer_checker import integer_checker

CAP = 100
PI = 3.14159265359
history = []

def find_quadralateral(type):
  # rename variables depending on quadrilateral type
  type = type
  if type == 1:
    print("SQUARE")
    shape, base_type, side_type = "Square", "length", "none"
  elif type == 2:
    print("RECTANGLE")
    shape, base_type, side_type = "Rectangle", "length", "width"
  elif type == 3:
    print("PARALLELOGRAM")
    shape, base_type, side_type = "Parallelogram", "base", "height"
  # calculate
  base = integer_checker("Enter the {}: ".format(base_type), CAP)
  if type != 1:
    a = integer_checker("Enter the {}: ".format(side_type), CAP)
  else:
    a = base
  perimeter = base + base + a + a
  area = base * a
  print("Area: {}, Circumference: {}".format(area, perimeter))
  result = f"Area: {area}, Perimeter: {perimeter}"
  history.append(f"{shape}: {result}")
  return

def find_circle():
  print("CIRCLE")
  shape = "Circle"
  base = integer_checker("Enter the radius: ", CAP)
  perimeter = 2 * PI * base
  area = PI * (base * base)
  print("Area: {}, Circumference: {}".format(area, perimeter))
  result = f"Area: {area}, Circumference: {perimeter}"
  history.append(f"{shape}: {result}")
  return

def find_triangle():
  print("TRIANGLE")
  shape = "Triangle"
  base = integer_checker("Enter the base: ", CAP)
  a = integer_checker("Enter side A: ", CAP)
  b = integer_checker("Enter side B: ", CAP)
  c = integer_checker("Enter the height: ", CAP)
  perimeter = base + a + b
  area = 0.5 * base * c
  print("Area: {}, Perimeter: {}".format(area, perimeter))
  result = f"Area: {area}, Perimeter: {perimeter}"
  history.append(f"{shape}: {result}")
  return
  
def find_trapezoid():
  print("TRAPEZOID")
  shape = "Trapezoid"
  base = integer_checker("Enter the long base: ", CAP)
  a = integer_checker("Enter the short base: ", CAP)
  b = integer_checker("Enter side A: ", CAP)
  c = integer_checker("Enter side B: ", CAP)
  d = integer_checker("Enter the height: ", CAP)
  perimeter = base + a + b + c
  area = ((base + a)*0.5)*d
  print("Area: {}, Perimeter: {}".format(area, perimeter))
  result = f"Area: {area}, Perimeter: {perimeter}"
  history.append(f"{shape}: {result}")
  return

def see_history():
  print("HISTORY")
  if not history:
    print("There is no input history")
  else:
    for item in history:
      print(item)