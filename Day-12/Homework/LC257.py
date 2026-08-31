class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        result = []

        def dfs(node, path):
            if not node.left and not node.right:
                result.append(path + str(node.val))
                return
            if node.left:
                dfs(node.left, path + str(node.val) + '->')
            if node.right:
                dfs(node.right, path + str(node.val) + '->')

        dfs(root, '')
        return result
