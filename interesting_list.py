num_list = [-2, 33, 14, 6, -13, 9, 2]

# def make_interesting_list(num_list):
    
# num_list = [elem for elem in num_list if elem >= 0 and elem % 2 == 0]
# print(num_list)

# no need for the assignment: elem = elem + 10
num_list = [elem + 10 if elem >= 0 and elem % 2 == 1 else elem for elem in num_list if elem >= 0 and elem % 2 == 0]
print(num_list)


    # new_list = []
    # return num_list

    #     if elem >= 0 and elem % 2 == 0 :
    #        elem = elem
    #        new_list.append(elem)
    #     else:
    #        elem = elem + 10
    #        new_list.append(elem)

    # return new_list
  

# print(make_interesting_list(num_list))