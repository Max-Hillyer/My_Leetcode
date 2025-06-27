#Max Hillyer 4/27/25

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s += " "
        hash = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            " " : 0
        }
        num = 0

        for i in range(len(s) - 1):
            if hash.get(s[i]) < hash.get(s[i+1]):
                num -= hash.get(s[i])
            else:
                num += hash.get(s[i])
        return(num)

        
