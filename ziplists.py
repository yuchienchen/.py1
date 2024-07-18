"""
File: ziplists.py
-----------------
This program gives you practice working with a list of lists.
"""


def zip2lists(list1, list2):
    """
    This function is passed two lists of strings.  Both lists both have
    the same length.  The function returns a new list that "zips" together
    the two lists passed in into a list that contains lists that are pairs of
    elements, one from each of the original lists, in order.  For example, if
    this function were passed the lists ['a', 'b', 'c'] and ['d', 'e', 'f'] it
    would return the list of lists:
    [['a', 'd'], ['b', 'e'], ['c', 'f']]
    The original lists passed in should not be changed.
    Note that if this function is passed two empty lists, it should just
    return an empty list, since there would be no lists (of pairs) in the
    result.
    >>> zip2lists(['a', 'b', 'c'], ['d', 'e', 'f'])
    [['a', 'd'], ['b', 'e'], ['c', 'f']]
    >>> zip2lists(['one'], ['two'])
    [['one', 'two']]
    >>> zip2lists([], [])
    []
    """
    grid = []
    sub_list1 = []
    sub_list1.append(list1[0])
    sub_list1.append(list2[0])
    print(sub_list1)

    sub_list2 = []
    sub_list2.append(list1[1])
    sub_list2.append(list2[1])
    print(sub_list2)

    sub_list3 = []
    sub_list3.append(list1[2])
    sub_list3.append(list2[2])
    print(sub_list3)

    grid.append(sub_list1)
    grid.append(sub_list2)
    grid.append(sub_list3)
    return grid

    # for i in range(len(list1)) and range(len(list2)):
    #     sub_list.append(list1[i])
    #     sub_list.append(list2[i])
    # print(sub_list)


def main():
    result_list = zip2lists(['a', 'b', 'c'], ['d', 'e', 'f'])
    print(result_list)      # should print [['a', 'd'], ['b', 'e'], ['c', 'f']]


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
