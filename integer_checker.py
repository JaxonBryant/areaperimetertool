
def integer_checker(question, CAP):
  CAP = float(CAP)
  # loop for testing
  notvalid = True  
  # create loop
  while notvalid:
    # force integer/float input
    try:
      user_input = float(input(question))
    except ValueError:
      print("Input must be a number")
      continue
    user_input = round(user_input, 2)
    if not (0 < user_input < CAP + 1):
      print("Input must be above 0 and below {}".format(CAP))
      continue
    notvalid = False
    print("")
    return user_input

    


#def integer_checke(question, CAP):
  #set up loop to force valid input
  #while True:
    #formatting
    #user_input = input(question).strip()
    # prevent blank inputs
    #if user_input == "":
      #print("Error, input cannot be blank ")
      #continue
    # prevent strings
    #if not user_input.isdigit():
      #print("Error, input must be a positive number ")
      #continue
    # offically convert string into float
    #user_input = float(user_input)
    # prevent input 0 or anything above CAP
    #if user_input == 0 or user_input >= CAP + 0.01:
      #print("Error, input must be above 0 and below {}".format(CAP))
      #continue
    #return user_input