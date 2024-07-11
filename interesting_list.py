# num_list = [-2, 33, 14, 6, -13, 9, 2]

def make_interesting_list(num_list):
    
    new_list = []
    for elem in num_list:
        if elem < 0:
           del elem
        if elem >= 0 and elem % 2 == 0 :
           elem = elem
           new_list.append(elem)
        else:
           elem = elem + 10
           new_list.append(elem)

    return new_list
  

print(make_interesting_list([-2, 33, 14, 6, -13, 9, 2]))