def main():
    month_values = [[1,2,3,4,5,6,7,8,9,10,11,12],
                [3,0,0,0,0,0,0,0,0,0,0,0],
                [12,0,0,0,0,0,0,0,0,0,0,0]]
    nested = month_values
    print(annual_temps(nested))

def annual_temps(nested):
    ave_temps = []
    rows = len(nested)
    cols = len(nested[0])
    for i in range(rows):
        print(nested[i])
        print(sum(nested[i]))
        average_temp = sum(nested[i]) / len(nested[i])
        print(average_temp)
        ave_temps.append(average_temp)
    
    return ave_temps

        # for j in range(cols):
        #     print(nested[i][j])
        #     average_temp =  / len(nested[i])


if __name__ == '__main__':
    main()