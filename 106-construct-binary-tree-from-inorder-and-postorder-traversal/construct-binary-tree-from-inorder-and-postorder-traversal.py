# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        postorder=list(postorder)
        def tr(p,i):
            if i and p:
                id=i.index(p.pop())
                root=TreeNode(i[id])
                root.left=tr(p[:id],i[:id])
                root.right=tr(p[id:],i[id+1:])
                return root



        return tr(postorder,inorder)



        