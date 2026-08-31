class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def dfs(node, path, remaining):
            if not node:
                return
            path.append(node.val)
            remaining -= node.val
            if not node.left and not node.right and remaining == 0:
                result.append(path[:])
            dfs(node.left, path, remaining)
            dfs(node.right, path, remaining)
            path.pop()

        dfs(root, [], targetSum)
        return result
