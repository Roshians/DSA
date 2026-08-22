arr = [1,2,3,4]

# Prefix
def prefix(arr):
    sum = 0
    for i in range(len(arr)):
        arr[i] += sum
        sum += arr[i]
    return arr

def sufix(arr):
    sum = 0
    for i in range(len(arr)-1, -1, -1):
        arr[i] += sum
        sum += arr[i]
    return arr

