def main():
    grid = [[None, None, None],
        [None, None, None],
        [None, 'f' , None],
        [None, None, None]]
    explode_firewords(grid)

def explode_firewords(grid):
    rows = len(grid)
    print(rows)
    cols = len(grid[0])
    print(cols)
    # for i in range(rows):
        # for j in range(cols):
        #     print(grid[i][j])


if __name__ == '__main__':
    main()