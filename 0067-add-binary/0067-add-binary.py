class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        s=[]
        car = 0 
        i = len(a)-1
        j = len(b)-1

        while i >=0 or j >=0 or car:
            if i>=0:
                car += int(a[i])
                i-=1
            if j>=0:
                car += int(b[j])
                j-=1
            
            s.append(str(car%2))
            car//=2
        
        return ''.join(reversed(s))
        