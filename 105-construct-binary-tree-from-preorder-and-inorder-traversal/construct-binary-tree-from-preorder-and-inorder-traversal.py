# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder=deque(preorder)
        def tr(p,i):
            if i:
                id=i.index(p.popleft())
                root=TreeNode(i[id])
                root.left=tr(p,i[:id])
                root.right=tr(p,i[id+1:])
                return root


        return tr(preorder,inorder)



        