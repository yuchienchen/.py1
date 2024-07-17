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
            grid = [grid[y][x] == None, grid[y - 1][x] == 's', grid[y + 1][x] == 's', grid[y][x - 1] == 's', grid[y][x + 1] == 's' if grid[y][x] == 'f' else None]
    print(grid)


            # if grid[y][x] == 'f':
            #     grid[y - 1][x] == 's'
            #     grid[y + 1][x] == 's'
            #     grid[y][x - 1] == 's'
            #     grid[y][x + 1] == 's'
            #     grid[y][x] == None
                


if __name__ == '__main__':
    main()