#Max Hillyer 6/26/25
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        list2 = []
        while l1:
            list1.append(l1.val)
            l1 = l1.next
        while l2:
            list2.append(l2.val)
            l2 = l2.next
        num1 = ''
        num2 = ''
        for i in list1[::-1]:
            num1 += str(i)
        for i in list2[::-1]:
            num2 += str(i)
        finalList = list((str(int(num1) + int(num2))[::-1]))
        
        head = ListNode(int(finalList[0]))
        current = head
        for i in range(1,len(finalList)):
            newNode = ListNode(int(finalList[i]))
            current.next = newNode
            current = newNode
        return head
        
        