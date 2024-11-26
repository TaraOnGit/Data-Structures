#Left array is always sorted.
arr = [6,5,7,4,8,3,2,9,1]
n = len(arr)

for i in range(1,n):
    for j in range(i,0,-1):
        if arr[j] < arr[j-1]:
            arr[j-1],arr[j] = arr[j],arr[j-1]
        else:
            break

print(arr)
'''
TC - O(n^2)
SC - O(1)
'''


