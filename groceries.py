# start over

# def get_list():
lst = []
elem = input("")
while elem != "":
    lst.append(elem)
    elem = input("")

print(lst)

# store lists in a grid
# def build_grid(roster):
grid = []
grid.append(lst)

print(grid)

# def get_groceries(index, grid):
#     type_list = []
#     rows = len(grid)
#     cols = len(grid[0])
#     for i in range(rows):
#         for index in range(cols):
#             print(grid[i][index])
#             type_list.append(grid[i][index])
        
#     return type_list

def main():
    pass
    # roster = get_list()
    # build_grid(roster)
    # get_groceries(index, grid)


if __name__ == '__main__':
    main()