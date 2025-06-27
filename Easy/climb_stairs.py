#max hillyer 4/29/25

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        a,b = 1,2
        for _ in range(n-1):
            a,b = b,a+b
        return a
        
