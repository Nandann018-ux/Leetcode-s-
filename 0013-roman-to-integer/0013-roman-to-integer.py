class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        value = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}

        tot = 0
        n = len(s)

        for i in range(n):
            if i < n - 1 and value[s[i]] < value[s[i + 1]]:
                tot-= value[s[i]]
            else:
                tot+= value[s[i]]
    
        return tot


        