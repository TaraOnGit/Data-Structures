def rev1(s):
    return s[::-1]

'''
TC - O(n)
SC - O(n)
'''

def rev2(s):
    res = []
    for i in range(len(s)-1,-1,-1):
        res.append(s[i])
    return ''.join(res)

'''
TC - O(n)
SC - O(n)
'''

print(rev1('hello world'))
print(rev2('hello world'))