# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        r=[]
        def t(root):
            if not root:
                return None
            t(root.left)
            r.append(root.val)
            t(root.right)


        t(root)
        return r
        