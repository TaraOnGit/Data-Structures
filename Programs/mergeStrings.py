''' Merge Strings Alternately
You are given two strings word1 and word2. Merge the
strings by adding letters in alternating order, starting
with word1. If a string is longer than the other, append
the additional letters onto the end of the merged string.
'''

# Lists are better than string concatenation.

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        mer = []
        size = max(len(word1), len(word2))
        for i in range(0, size):
            if i < len(word1):
                mer.append(word1[i])
            if i < len(word2):
                mer.append(word2[i])
        return ''.join(mer)


obj = Solution()
print(obj.mergeAlternately('Taj', 'Mahal'))

'''
TC - O(n)
SC - O(n)
'''







