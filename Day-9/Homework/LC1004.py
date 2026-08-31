class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        ones = 0
        max_len = 0
        for right, num in enumerate(nums):
            if num == 1:
                ones += 1
            while right - left + 1 - ones > k:
                if nums[left] == 1:
                    ones -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len
