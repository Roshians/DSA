class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = {0: 1}

        def dfs(node, current):
            if not node:
                return 0
            current += node.val
            total = prefix.get(current - targetSum, 0)
            prefix[current] = prefix.get(current, 0) + 1
            total += dfs(node.left, current)
            total += dfs(node.right, current)
            prefix[current] -= 1
            if prefix[current] == 0:
                del prefix[current]
            return total

        return dfs(root, 0)
