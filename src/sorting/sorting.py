# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # Your code here

    # initialize left and right index as 0
    l, r = 0, 0
    # array where values will be appended as they're found (least to greatest)
    result = []

    # while the value of l is less than the length of arrA and r is less than arrB
    while l < len(arrA) and r < len(arrB):
        #if arrA[l] < arrB[r]
        if arrA[l] < arrB[r]:
            # append arrA[l] to the results array (remember, least go in first)
            result.append(arrA[l])
            # add 1 to change index
            l += 1
        # otherwise arrB[r] is least...
        else:
            # so append that one instead
            result.append(arrB[r])
             # add 1 to change index
            r += 1
    result += arrA[l:]
    result += arrB[r:]
    return result

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:  # base case
        return arr

    # divide array in half and merge sort recursively
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

