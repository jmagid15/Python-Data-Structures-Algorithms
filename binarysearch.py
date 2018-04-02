def binarysearch(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


def binarysearch_rec(arr, left, right, target):
    if left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            return binarysearch_rec(arr, mid+1, right, target)

        else:
            return binarysearch_rec(arr, left, mid-1, target)

    else:
        return -1
