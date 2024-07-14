# initializes an empty list to store the lists
grid = []

def get_list_build_grid():
    # keeps generating new lists until the user inputs an empty list
    while True:
        lst = []
        elem = input("")
        # collects elements from the user until an empty string is entered
        while elem != "":
            lst.append(elem)
            elem = input("")
        print(lst)
        # breaks the loop if the list is empty
        if lst == []:
            break

        # adds the generated list to the grid
        grid.append(lst)
        # prints the current state of the grid after each new list is added
        print("Current grid: ", grid)
    # prints the final grid after the loop ends
    print("Final grid: ", grid)    

# def get_groceries(index, grid):
    type_list = []
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for index in range(cols):            
            if index == 1:
                type_list.append(grid[i][index])
    print(type_list)

    for i in range(rows):
        for index in range(cols):            
            if index == 2:
                type_list.append(grid[i][index])
    print(type_list)

    for i in range(rows):
        for index in range(cols):            
            if index == 3:
                type_list.append(grid[i][index])
    print(type_list)
        
    # return type_list

def main():
    grid = get_list_build_grid()
    # index_type_list = get_groceries(index, grid)
    # print(index_type_list)


if __name__ == '__main__':
    main()