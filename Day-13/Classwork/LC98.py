# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def inorder(node, values):
            if not node:
                return True
            
            if not inorder(node.left, values):
                return False
            
            if values and node.val <= values[-1]:
                return False
            values.append(node.val)
            
            return inorder(node.right, values)
        
        return inorder(root, [])