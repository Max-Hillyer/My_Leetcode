#Max Hillyer 6/26/25

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n= len(nums)
        for i in range(n+1):
            if i not in nums:
                return i
