# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def f(root,k):
            if root is None:
                return None
            
            f(root.left,k)
            res.append(root.val)
            f(root.right,k)
        f(root,k)
        return res[k-1]

        
