#Adjacent elements are compared in each iteration
arr = [6,5,7,4,8,3,2,9,1]

n = len(arr)

for i in range(n):
    for j in range(n-i-1): # Sorted Last Elements = No. of completed iterations
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)

'''
TC - O(n^2)
SC - O(1)
'''