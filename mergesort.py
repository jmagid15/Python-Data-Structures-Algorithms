def mergesort(arr, left, right):
    if left < right:
        mid = (right + left) // 2
        mergesort(arr, left, mid)
        mergesort(arr, mid+1, right)
        merge(arr, left, mid, right)


def merge(arr, left, mid, right):
    left_arr = arr[left : mid + 1]
    right_arr = arr[mid + 1 : right + 1]

    i = j = 0
    master_i = left

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr[master_i] = left_arr[i]
            i += 1
        else:
            arr[master_i] = right_arr[j]
            j += 1
        master_i += 1

    while i < len(left_arr):
        arr[master_i] = left_arr[i]
        i += 1
        master_i += 1
