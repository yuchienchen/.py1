# create individual list
def get_grocery_list():

    grocery_list = []
    while True:
        user_input = input("")

        # If the user enters a blank line, break out of the loop and stop asking for input
        if user_input == "":
            break
    
        grocery_list.append(user_input)

    return grocery_list

def get_groceries(index, grid):
    pass