# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def getMaxDepth(curr, depth):
            if not curr:
                return depth
            currDepth = 1 + depth
            leftDepth = getMaxDepth(curr.left, currDepth)
            rightDepth = getMaxDepth(curr.right, currDepth)
            return max(leftDepth, rightDepth)
        
        return getMaxDepth(root, 0)
        
