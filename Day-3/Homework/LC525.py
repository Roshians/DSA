class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        balance = 0
        seen = {0: -1}
        best = 0

        for i, num in enumerate(nums):
            balance += 1 if num == 1 else -1
            if balance in seen:
                best = max(best, i - seen[balance])
            else:
                seen[balance] = i

        return best
