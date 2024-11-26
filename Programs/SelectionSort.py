#First element compared with rest of the elements in all iterations

arr = [6,5,7,4,8,3,2,9,1]

n = len(arr)

for i in range(n):
    for j in range(i+1,n):
        if arr[j] < arr[i]:
            arr[i], arr[j] = arr[j], arr[i]

print(arr)

'''
TC - O(n^2)
SC - O(1)

'''