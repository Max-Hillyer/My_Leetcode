#max hillyer 4/28/25

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        def decToBin(num):
            converted = ""
            num = int(num)
            if num == 0:
                return 0
            while num > 0:
                binDigit = str(num % 2)
                num = num // 2
                converted = binDigit + converted
            return converted
        def binToDec(num):
            if num == 0:
                return 0
            total = 0
            power = 1
            for digit in str(num)[::-1]:
                if digit == '1':
                    total += power
                power *= 2
            return total
        sum = binToDec(a)+binToDec(b)
        return(str(decToBin(sum)))
        
