class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.best = float('-inf')

        def dfs(node):
            if not node:
                return 0
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            self.best = max(self.best, left + right + node.val)
            return max(left, right) + node.val

        dfs(root)
        return self.best
