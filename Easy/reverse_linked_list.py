#max hillyer 6/26/25

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        vals.reverse()
        head = ListNode(vals[0])
        current = head
        for i in range(1,len(vals)):
            newNode = ListNode(vals[i])
            current.next = newNode
            current = newNode
        return head
