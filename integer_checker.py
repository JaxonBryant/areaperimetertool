"""Stores integer_checker function."""


def integer_checker(question, cap):
    """Force valid input."""


    cap = float(cap)
    # loop for testing
    not_valid = True
    # create loop
    while not_valid:
        # force integer/float input
        try:
            user_input = float(input(question))
        except ValueError:
            print("Input must be a number")
            continue
        # force input between 0 and program capacity
        user_input = round(user_input, 2)
        if not (0 < user_input < cap + 1):
            print("Input must be above 0 and below {}".format(cap))
            continue
        not_valid = False
        print("")
        return user_input
