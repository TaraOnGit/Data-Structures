arr = [5,6,4,3,7,8,1,2,9]

lowest = arr[0]

for i in range(1,len(arr)):
    if arr[i] < lowest:
        lowest = arr[i]

print(lowest)

'''
TC - O(n)
SC - O(1)
'''