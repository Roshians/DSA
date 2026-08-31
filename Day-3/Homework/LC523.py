class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = 0
        seen = {0: -1}

        for i, num in enumerate(nums):
            prefix = (prefix + num) % k if k != 0 else prefix + num
            if prefix in seen:
                if i - seen[prefix] >= 2:
                    return True
            else:
                seen[prefix] = i

        return False
