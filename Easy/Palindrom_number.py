#Max Hillyer 4/27/25
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        list = [str(i) for i in str(x)]
        if list == list[::-1]:
            return True
        return False
