def quick(arr):

    if len(arr) > 0:
        pivot = arr[0]

        left = [i for i in arr if i < pivot]
        middle = [i for i in arr if i == pivot]
        right = [i for i in arr if i > pivot]

        return quick(left) + middle + quick(right)
    else:
        return arr

def squares(arr):
    sorted_arr = quick(arr)
    low, high = 0, len(sorted_arr) - 1
    res = [0] * len(sorted_arr)
    while low < high:
        res[low] = sorted_arr[low] ** 2
        res[high] = sorted_arr[high] ** 2
        low += 1
        high -= 1
    return res

print(squares([1,2,3,4,5,6]))




