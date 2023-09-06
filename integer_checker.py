
def integer_checker(question, CAP):
  #set up loop to force valid input
  while True:
    #formatting
    print("")
    user_input = input(question).strip()
    # prevent blank inputs
    if user_input == "":
      print("Error, input cannot be blank ")
      continue
    # prevent strings
    if not user_input.isdigit():
      print("Error, input must be a positive number ")
      continue
    # offically convert string into float
    user_input = float(user_input)
    # prevent input 0 or anything above CAP
    if user_input == 0 or user_input >= CAP + 0.01:
      print("Error, input must be above 0 and below {}".format(CAP))
      continue
    return user_input