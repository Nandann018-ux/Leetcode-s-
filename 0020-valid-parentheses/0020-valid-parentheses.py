class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        prev = None
        while prev != s:   
            prev = s
            s = s.replace("()", "").replace("{}", "").replace("[]", "")
        return s == ""