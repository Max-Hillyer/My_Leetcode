#max Hillyer 6/24/25

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        current = root
        path = []
        final = []
        while current or path:
            while current: #get to leftmost item and record the path
                path.append(current)
                current = current.left
            current = path.pop()
            final.append(current.val)
            current = current.right
        return final

    
