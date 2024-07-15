def main():
    month_values = [[1,2,3,4,5,6,7,8,9,10,11,12],
                [3,0,0,0,0,0,0,0,0,0,0,0],
                [12,0,0,0,0,0,0,0,0,0,0,0]]
    nested = month_values
    annual_temps(nested)

def annual_temps(nested):
    # ave_temps = []
    rows = len(nested)
    cols = len(nested[0])
    for i in range(rows):
        for j in range(cols):
            print(nested[i][j])


if __name__ == '__main__':
    main()