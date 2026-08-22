def mergeSort(arr, left, right):
    if left >= right:
        return
    mid = (left + right) // 2

    mergeSort(arr, left, mid)
    mergeSort(arr, mid + 1, right)
    merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    temp = []
    i = left
    m