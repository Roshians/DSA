class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = 0
        counts = {0: 1}
        total = 0

        for num in nums:
            prefix = (prefix + num) % k
            total += counts.get(prefix, 0)
            counts[prefix] = counts.get(prefix, 0) + 1

        return total
