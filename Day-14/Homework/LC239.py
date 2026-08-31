class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        dq = []
        result = []

        for i, num in enumerate(nums):
            while dq and dq[0] <= i - k:
                dq.pop(0)
            while dq and nums[dq[-1]] <= num:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                result.append(nums[dq[0]])
        return result
