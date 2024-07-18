"""
File: removeduplicates.py
-------------------------
This program gives you practice with constructing a new list
based on values given to you by the user.  You also get
practice removing duplicates from that list
"""


def read_list():
    """
    This function should ask the user for a series of integer values
    (until the user enters 0 to stop) and store all those values in a
    list.  That list should then be returned by this function.
    """
    list = []
    while True:
        user_input = int(input("Enter value (0 to stop): "))
        if user_input == 0:
            break
        num = int(user_input)
        list.append(user_input)

    return list

def remove_duplicates(num_list):
    """
    This function is passed a list of integers and returns a new
    list with all duplicate values from the original list remove.
    >>> remove_duplicates([1, 2, 3, 2, 3, 4])
    [1, 2, 3, 4]
    >>> remove_duplicates([1, 1, 1])
    [1]
    >>> remove_duplicates([])
    []
    """
    num_dict = {}
    for num in num_list:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    
    print(num_dict)

    for key, value in num_dict.items():
        if value > 1:
            

    # update_list = []

    # update_list.append()

    # return update_list

def main():
    num_list = read_list()
    print("Original list entered by user: ")
    print(num_list)

    no_duplicates = remove_duplicates(num_list)
    print("List with duplicates removed: ")
    print(no_duplicates)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
