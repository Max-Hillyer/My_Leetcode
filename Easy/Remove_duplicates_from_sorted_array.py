#Max Hillyer 6/27/25
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len(set(nums)),list(set(nums))
        
