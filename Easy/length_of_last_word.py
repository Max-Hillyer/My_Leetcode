#max hillyer 4/28/25

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        list_s = s.split()
        return len(list_s[-1])
