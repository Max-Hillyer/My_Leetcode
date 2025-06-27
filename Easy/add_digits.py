#max hillyer 6/26/25

class Solution:
    def addDigits(self, num: int) -> int:
        if len(str(num)) == 1:
            return num
        num = str(num)
        final = 0
        for i in num:
            final += int(i)
        return self.addDigits(final)
        
        
