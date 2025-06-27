#max hillyer 4/27/25

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        longest = strs[0]
        for word in strs:
            while not word.startswith(longest):
                longest = longest[:-1]
                if not longest:
                    break
        if longest:
            return longest
        return ""
        
        
