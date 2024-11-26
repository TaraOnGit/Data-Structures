def squares(arr):
    left, right = 0, len(arr)-1
    res = [0] * len(arr)
    while left <= right:
        res[left] = arr[left] ** 2
        res[right] = arr[right] ** 2
        left += 1
        right -= 1
    return res

print(squares([1,2,3,4,5,6]))
'''
TC - O(n)
SC - O(n)
'''