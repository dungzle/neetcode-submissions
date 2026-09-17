# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.result = True
        def dfs(tree1, tree2):
            if self.result == False:
                return False
            if not tree1 and not tree2:
                return True
            if (not tree1 and tree2) or (tree1 and not tree2) or (tree1.val != tree2.val):
                self.result = False
                return False
            return dfs(tree1.left, tree2.left) and dfs(tree1.right, tree2.right)
        self.result = dfs(p,q)
        return self.result
            