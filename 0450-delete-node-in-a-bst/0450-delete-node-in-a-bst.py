# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def suc(root):
            node = root.right
            while node.left:
                node = node.left
            return node.val
        
        def f(root,key):
            
            if root is None:
                return None

            if root.val < key:
                root.right = self.deleteNode(root.right,key)
            elif root.val > key:
                root.left = self.deleteNode(root.left,key)
            else:
                if root.left is None and root.right is None:
                    return None
                if root.left is None:
                    return root.right
                if root.right is None:
                    return root.left
                root.val = suc(root)
                root.right = f(root.right,root.val) 
            return root
        return f(root,key)
        

        