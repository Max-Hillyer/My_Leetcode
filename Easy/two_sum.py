#Max Hillyer 4/25/25

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                 if nums[j] + nums[i] == target and i != j:
                    return i,j
