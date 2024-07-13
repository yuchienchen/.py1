# create individual list
# for i in range(3):
#     list = []
#     for i in range(4):
#         list.append(input(""))

#     print(list)

store1 = ["Trader Joe's", 'Banana', 'Kale', 'Baguette']
store2 = ['H-Mart', 'Mango', 'Broccoli', 'Buns']
store3 = ['Munger Market', 'Apple', 'Salad mix', 'Cookie']

# store lists in a grid
grid = []
# grid = [store1] + [store2] + [store3]
# for i in range(3):
grid.append(store1)
grid.append(store2)
grid.append(store3)

print(grid)

# def get_groceries(index, grid):

type_list = []
rows = len(grid)
cols = len(grid[0])
for i in range(rows):
    for index in range(cols):
        print(grid[i][index])
#         type_list.append(grid[i][index])
    
# print(type_list)

# def main():
#     get_groceries(index, grid)


# if __name__ == '__main__':
#     main()