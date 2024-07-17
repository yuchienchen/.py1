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
                grid = [grid[y][x] == None, 
                        grid[y - 1][x] == 's' if y - 1 >= 0 else False,
                        grid[y + 1][x] == 's' if y + 1 < rows else False, 
                        grid[y][x - 1] == 's' if x - 1 >= 0 else False,  
                        grid[y][x + 1] == 's' if x + 1 < cols else False,]
                print(grid)
            
            #     grid[y - 1][x] == 's'
            #     grid[y + 1][x] == 's'
            #     grid[y][x - 1] == 's'
            #     grid[y][x + 1] == 's'
            #     grid[y][x] == None
                


if __name__ == '__main__':
    main()