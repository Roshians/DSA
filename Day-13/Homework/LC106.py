class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None

        root_val = postorder[-1]
        root_index = inorder.index(root_val)
        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index + 1:]

        left_postorder = postorder[:len(left_inorder)]
        right_postorder = postorder[len(left_inorder):-1]

        root = TreeNode(root_val)
        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)
        return root
