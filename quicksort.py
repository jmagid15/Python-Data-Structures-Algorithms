# def quicksort(arr=[12,4,5,6,7,3,1,15]):
#     less = []
#     equal = []
#     greater = []
#
#     if len(arr) > 1:
#         pivot = arr[0]
#         for x in arr:
#             if x < pivot: # less than
#                 less.append(x)
#             elif x == pivot: # equal to
#                 equal.append(x)
#             else: # greater than
#                 greater.append(x)
#         # Don't forget to return something!
#         return quicksort(less) + equal + quicksort(greater)  # The + operator joins lists
#     else:  # Return arr if just one element
#         return arr

def swap(arr, left, right):
    arr[left], arr[right] = arr[right], arr[left]


def partition(arr, left, right):
    wall = left
    i = left
    pivot_val = arr[right]

    while i < right:
        if arr[i] < pivot_val:
            swap(arr, wall, i)
            wall += 1
        i += 1

    swap(arr, wall, right)

    return wall


def quicksort(arr, left, right):
    if left < right:
        idx = partition(arr, left, right)
        quicksort(arr, left, idx-1)
        quicksort(arr, idx+1, right)
