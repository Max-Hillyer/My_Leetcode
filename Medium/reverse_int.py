#max hillyer 6/27/25

class Solution:
    def reverse(self, x: int) -> int:
        thelist = [str(i) for i in str(x)]
        thelist.reverse()
        if '-' in thelist:
            thelist.remove('-')
            print(thelist)
            neg = True
        else:
            neg = False
        final = int("".join(thelist))
        if final > 2**31 - 1 or final < -2**31:
            return 0
        if neg:
            return final - 2*final
        return final

