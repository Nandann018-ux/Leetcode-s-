class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res = []
        n = min(len(word1), len(word2))

        for i in range(n):
            res.append(word1[i]+word2[i])
        
        res.append(word1[n:] + word2[n:])
        
        return ''.join(res)
