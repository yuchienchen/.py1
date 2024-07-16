def main():
    grid = [[None, None, None],
        [None, None, None],
        [None, 'f' , None],
        [None, None, None]]
    explode_fireworks(grid)

def explode_fireworks(grid):
    rows = len(grid)
    # print(rows)
    cols = len(grid[0])
    # print(cols)
    for y in range(rows):
        for x in range(cols):
            # print(grid[y][x])
            if grid[y][x] == 'f':
                grid[y - 1][x] == 's'
                grid[y + 1][x] == 's'
                grid[y][x - 1] == 's'
                grid[y][x + 1] == 's'
                grid[y][x] == None
                
def swap(grid, row1, col1, row2, col2):
    temp = grid[row1][col1]
    grid[row1][col1] = grid[row2][col2]
    grid[row2][col2] = temp


if __name__ == '__main__':
    main()