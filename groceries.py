
def get_list_build_grid():
    # initializes an empty list to store the lists
    grid = []
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

def get_groceries(index, grid):
    print(grid)
    fruit_list = []
    vege_list = []
    carbs_list = []
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for index in range(cols):            
            if index == 1:
                fruit_list.append(grid[i][index])
            if index == 2:
                vege_list.append(grid[i][index])
            if index == 3:
                carbs_list.append(grid[i][index])

    print(fruit_list)            
    print(vege_list)
    print(carbs_list)
        
    # return type_list

def main():
    grid = get_list_build_grid()
    # print(grid)
    index = input("Enter a number: ")
    get_groceries(index, grid)

    if index == 1: 
        print(get_groceries(index, grid))
    if index == 2:
        print(get_groceries(index, grid))
    if index == 3:
        print(get_groceries(index, grid))


if __name__ == '__main__':
    main()