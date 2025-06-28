#max hillyer 6/27/25

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        finalList = []
        for i in lists:
            while i:
                finalList.append(i.val)
                i = i.next
        finalList.sort()
        if not finalList:
            return None
        head = ListNode(finalList[0])
        current = head
        for i in range(1,len(finalList)):
            newNode = ListNode(finalList[i])
            current.next = newNode
            current = newNode
        return head
        

