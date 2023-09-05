
from integer_checker import integer_checker

def multi_choice(CAP):
  choice = integer_checker("Choose an option, 1-6: ", CAP)
  if choice == 1:
    print("1")
  if choice == 2:
    print("2")
  if choice == 3:
    print("3")
  if choice == 4:
    print("4")
  if choice == 5:
    print("5")
  if choice == 6:
    print("6")