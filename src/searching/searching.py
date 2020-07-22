# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    #mid equals the start and the end index divided by two and floored.
    mid = (start + end) // 2  

    #check for stupid arguments
    if end is None:
        end = len(arr) - 1
    if start > end:
        return -1

    # if target < arr[mid], then recurse except end is now mid-1
    # we want to forget the half that is greater than our target
    if target < arr[mid]:
        return binary_search(arr, target, start, mid-1)
    # if target > arr[mid], then recurse except start is now mid+1
    # we want to forget the half that is less than our target
    if target > arr[mid]:
        return binary_search(arr, target, mid+1, end)
    #check if target value is the same as arr[mid] value
    #return mid if it is
    if target == arr[mid]:
        return mid

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass