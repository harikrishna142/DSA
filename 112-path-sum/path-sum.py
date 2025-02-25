# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def path(root,t):
            if not root:
                return False
            if not root.left and not root.right and root.val==t:
                return True
            
            return path(root.left,t-root.val) or path(root.right,t-root.val)
        return path(root,targetSum)
            
        