
def collapse(lst):
    """
    Accepts a list of integers as a parameter and returns a new
    list containing the result of replacing each pair of integers
    with the sum of that pair.

    If the list stores an odd number of elements, the final element
    is not collapsed

    >>> nums = [7, 2, 8, 9, 4, 13, 7, 1, 9, 10]
    >>> collapse(nums)
    [9, 17, 17, 8, 19]
    >>> nums = [1, 2, 3, 4, 5]
    >>> collapse(nums)
    [3, 7, 5]
    """
    pass 

# nums = [1, 2, 3, 4, 5]
# # for i in range(len(nums)):
# #     if len(nums) % 2 == 1:

# nums = [elem[i] + elem [i + 1] for i in range(len(nums)) ]
# nums = [nums[0] + nums[1], nums[2] + nums[3], nums[4]]

#     # return nums

# print(nums)

def distinct_elements(lst):
    """
    Returns a list of all the disinct elements in lst, in the order that
    they first occur in lst.
    >>> distinct_elements([1, 2, 3, 4])
    [1, 2, 3, 4]
    >>> distinct_elements([1, 1, 2, 2, 3])
    [1, 2, 3]
    >>> distinct_elements(['hello', 'hello', 'hello', 'hello', 'hello'])
    ['hello']
    >>> distinct_elements([])
    []
    """
    pass

def rotate_list_right(lst, n):
    """
    returns a 'rotate' version of the list that rotates numbers
    to the right n times. Each element in numbers is shifted
    forward n places, and the last n elements are moved to
    the start of the list.

    Your function should not change the list that is passed as a
    parameter.

    >>> rotate_list_right([1, 2, 3, 4, 5], 2)
    [4, 5, 1, 2, 3]
    """

    lst = []
    for i in range(len(lst)):
        lst[i] = lst[i + n]
    
    return lst

print(rotate_list_right([1, 2, 3, 4, 5], 2))