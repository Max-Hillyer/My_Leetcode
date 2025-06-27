#max hillyer 6/26/25

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numsDict = {}
        for i in nums:
            if i in numsDict.keys():
                numsDict[i] += 1
            else:
                numsDict[i] = 1
        
        for i in numsDict.keys():
            if numsDict.get(i) == max(list(numsDict.values())):
                return i
