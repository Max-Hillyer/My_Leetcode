#max hillyer 6/24/25

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i,item in enumerate(nums2):
            nums1[m+i] = item
        nums1.sort()
        
