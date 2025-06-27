#max hillyer 6/26/25

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new = set()
        for i in nums:
            if i in new:
                return True
            new.add(i)
        return False
