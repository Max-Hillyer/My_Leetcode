#max hillyer 6/25/25

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ''
        for i in s:
            if i.isalnum():
                newS += i
        return newS.lower() == newS.lower()[::-1]
        
